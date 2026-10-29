import os, re, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from tqdm import tqdm
import lhefunctions

HBAR_C = 1.973269804e-16  # GeV*m
MX = 15.0
OUT = "../../output_folds"
RUN_DIAGNOSTICS = True
L_INNER, L_OUTER = 0.0, 0.3  # m

# ------------------------------------------------------------------
# Operator table: name -> (group, events-dir prefix, EXP colour, TH colour)
# ------------------------------------------------------------------
lep_ex = ["#003f5c", "#2f4b7c", "#665191", "#a05195"]
lep_th = ["#d45087", "#f95d6a", "#ff7c43", "#ffa600"]
had_ex = ["#800000", "#9A0000", "#B22222", "#C73E1D", "#E03C31", "#EE6055", "#FA8072"]
had_th = ["#00441b", "#006d2c", "#238b45", "#41ab5d", "#66c2a4", "#80cd99", "#a6bdbb"]

lep_ops = ["cXe", "cXl", "cdhielx", "cdhieslx"]
had_ops = ["cXq", "cXd", "cXu", "cdhidqx", "cdhidsqx", "cdhiqux", "cdhiqsux"]

OPS = {}
for i, n in enumerate(lep_ops):
    OPS[n] = dict(group="lep", evdir=f"{OUT}/{n}_ppZXll_BSMEFT_lamscan2_15/Events/",
                  c_ex=lep_ex[i], c_th=lep_th[i], ex_style="o-", th_style="s--")
for i, n in enumerate(had_ops):
    OPS[n] = dict(group="had", evdir=f"{OUT}/{n}_R_ppZXll_BSMEFT_lamscan2_15/Events/",
                  c_ex=had_ex[i], c_th=had_th[i], ex_style="^-", th_style="d--")

lamX = np.array([10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1000, 2000, 3000, 5000, 7000, 10000])
valid = lamX > 91


# ------------------------------------------------------------------
# I/O helpers
# ------------------------------------------------------------------
def read_partial_widths(filepath):
    vals, errs = [], []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fields = line.split()
            if len(fields) >= 5:
                vals.append(float(fields[2])); errs.append(float(fields[3]))
            if len(fields) == 2:
                vals.append(float(fields[0])); errs.append(float(fields[1]))
    return np.array(vals), np.array(errs)


def collect_X_kinematics(paths, pid=9000002, cache=None):
    """Parse LHE once (cached to .npz); return per-X arrays plus per-event X multiplicity."""
    if cache and os.path.exists(cache):
        return dict(np.load(cache))
    out = {k: [] for k in ["px", "py", "pz", "E", "m_lhe", "nX"]}
    for run_path in tqdm(paths, desc=os.path.basename(os.path.dirname(os.path.dirname(run_path_safe(paths))))):
        lhe_file = f"{run_path}/unweighted_events.lhe.gz"
        if not os.path.exists(lhe_file):
            continue
        for event in lhefunctions.read_lhe_outgoing(lhe_file):
            nX = 0
            for p in event:
                if abs(p["pid"]) != pid:
                    continue
                nX += 1
                out["px"].append(p["px"]); out["py"].append(p["py"]); out["pz"].append(p["pz"])
                # adjust key names if your lhefunctions uses different ones
                out["E"].append(p.get("E", p.get("e", p.get("energy", np.nan))))
                out["m_lhe"].append(p.get("m", p.get("mass", np.nan)))
            out["nX"].append(nX)
    out = {k: np.array(v, dtype=float) for k, v in out.items()}
    out["p"] = np.sqrt(out["px"]**2 + out["py"]**2 + out["pz"]**2)
    out["pT"] = np.hypot(out["px"], out["py"])
    out["m_calc"] = np.sqrt(np.clip(out["E"]**2 - out["p"]**2, 0, None))
    if cache:
        np.savez(cache, **out)
    return out


def run_path_safe(paths):
    return paths[0] if paths else "."


def pdecay_from_kin(kin, ctau_scan, mx, l_inner=L_INNER, l_outer=L_OUTER):
    bg = kin["p"] / mx
    res = []
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        for ctau in ctau_scan:
            L = bg * ctau
            P = np.exp(-l_inner / L) * (-np.expm1(-(l_outer - l_inner) / L))
            res.append(np.nanmean(P))
    return np.array(res)


# ------------------------------------------------------------------
# THEORY: ctau from X->Zll widths, BR from Z->Xll widths
# ------------------------------------------------------------------
Z_TOT = 2.495  # GeV
for n, d in OPS.items():
    w_xz, _ = read_partial_widths(f"{OUT}/{n}_XZll_BSMEFT_lamscan_15_results.txt")
    w_zx, _ = read_partial_widths(f"{OUT}/{n}_ZXll_BSMEFT_lamscan_15_results.txt")
    d["ctau_th"] = HBAR_C / w_xz
    d["br_th"] = w_zx / Z_TOT

# ------------------------------------------------------------------
# EXPERIMENT: BR95 = N95 / (Lumi * sigma * <P_decay>)
# ------------------------------------------------------------------
ctau_scan = np.logspace(-13, 4, 200)
cross, _ = read_partial_widths(f"{OUT}/ppZ_BSMEFT_lamscan_results.txt")
sigma_ppZ = np.mean(cross)  # pb
Lumi = 3.0e6                # pb^-1
N95 = -np.log(0.05)

kin, pdecay = {}, {}
for n, d in OPS.items():
    paths = sorted(glob.glob(f"{d['evdir']}/run_*"), key=lambda x: int(os.path.basename(x).split("_")[-1]))
    d["paths"] = paths
    if not paths:
        print(f"Warning: no run dirs for {n}")
        kin[n] = None
        pdecay[n] = np.full_like(ctau_scan, np.nan)
    else:
        kin[n] = collect_X_kinematics(paths, cache=f"kin_cache_{n}.npz")
        pdecay[n] = pdecay_from_kin(kin[n], ctau_scan, MX)
    d["br95"] = N95 / (Lumi * sigma_ppZ * pdecay[n])

# ------------------------------------------------------------------
# DIAGNOSTICS
# ------------------------------------------------------------------
if RUN_DIAGNOSTICS:
    i_ref = np.argmin(np.abs(np.log10(ctau_scan) - 3))  # ctau ~ 1e3 m, rising region
    rows = []
    for n, k in kin.items():
        if k is None:
            continue
        bg = k["p"] / MX
        rows.append({
            "op": n, "N_X": len(bg), "<nX/evt>": k["nX"].mean(),
            "<m_LHE>": np.nanmean(k["m_lhe"]), "<m_calc>": np.nanmean(k["m_calc"]),
            "<bg>": bg.mean(), "median bg": np.median(bg),
            "<1/bg>^-1": 1.0 / np.mean(1.0 / bg),
            # P ~ l_out/(bg_eff*ctau) in the rising region
            "bg_eff(curve)": L_OUTER / (pdecay[n][i_ref] * ctau_scan[i_ref]),
            "frac bg<0.1": np.mean(bg < 0.1), "<pT_X>": k["pT"].mean(),
        })
    df = pd.DataFrame(rows).set_index("op")
    print(df.round(3).to_string())
    df.to_csv("diag_table.csv")

    # beta*gamma / pT / cumulative <1/bg> histograms
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))
    show = {"cXe": "k", "cXl": "b", "cdhielx": "tab:purple", "cXq": "r", "cdhidqx": "tab:orange"}
    for n, c in show.items():
        if kin.get(n) is None:
            continue
        bg = kin[n]["p"] / MX
        axes[0].hist(bg, bins=np.logspace(-3, 2, 80), histtype="step", density=True, color=c, label=n)
        axes[1].hist(kin[n]["pT"], bins=np.linspace(0, 60, 80), histtype="step", density=True, color=c, label=n)
        s = np.sort(bg); w = np.cumsum(1 / s)
        axes[2].plot(s, w / w[-1], color=c, label=n)
    axes[0].set(xscale="log", xlabel=r"$\beta\gamma_X$ (lab)", ylabel="density")
    axes[1].set(xlabel=r"$p_T^X$ [GeV]")
    axes[2].set(xscale="log", xlabel=r"$\beta\gamma_X$", ylabel=r"cumulative share of $\langle 1/\beta\gamma\rangle$")
    for a in axes:
        a.legend()
    plt.tight_layout(); plt.savefig("diag_bg.png", dpi=200); plt.close()

    # generation-setup comparison (banner)
    keys = ("ptl", "etal", "ptj", "etaj", "drll", "mmll", "ebeam1", "nevents", "lpp1", "MZ", "MX")
    for n in ["cXe", "cXl", "cdhielx", "cXq", "cdhidqx"]:
        p = OPS[n]["paths"]
        b = glob.glob(f"{p[0]}/*banner.txt") if p else []
        if not b:
            print(n, "no banner"); continue
        found = {}
        with open(b[0]) as f:
            for line in f:
                if line.startswith("#") or "=" not in line:
                    continue
                for k in keys:
                    if re.search(rf"\b{k}\b", line):
                        found[k] = line.split("!")[0].strip()
        print(n, found)

# ------------------------------------------------------------------
# PLOT
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 7))
handles, labels = [], []
hdr = lambda: mpatches.Rectangle((0, 0), 1, 1, fill=False, edgecolor="none", visible=False)

for grp, title in [("lep", "Leptonic"), ("had", "Hadronic")]:
    for kind in ["EXP", "TH"]:
        handles.append(hdr()); labels.append(rf"$\bf{{{title}\ Operators\ {kind}:}}$")
        for n, d in OPS.items():
            if d["group"] != grp:
                continue
            if kind == "EXP":
                (ln,) = ax.plot(ctau_scan, d["br95"], d["ex_style"], color=d["c_ex"], lw=2, ms=4)
            else:
                (ln,) = ax.plot(d["ctau_th"][valid], d["br_th"][valid], d["th_style"], color=d["c_th"], lw=2, ms=4)
            handles.append(ln); labels.append(rf"$({n.lower()})\ m_X = 15$ GeV")

ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(1e-13, 1e4)
ax.grid(True, which="both", alpha=0.3)
ax.set_xlabel(r"$c\tau$ [m]", fontsize=12)
ax.set_ylabel(r"95% CL Upper Limit on $\text{BR}_{Z \rightarrow X \ell^+\ell^-}$", fontsize=12)
ax.set_title(r"95% CL Upper Limit on Branching Ratio vs. Decay Length ($c = 1.0$)", fontsize=13)
ax.legend(handles, labels, bbox_to_anchor=(1.02, 1), loc="upper left", frameon=True, fontsize=8, ncol=2)
plt.tight_layout()
plt.savefig("plotBR95VBRthOPT.png", dpi=300, bbox_inches="tight")
plt.show()