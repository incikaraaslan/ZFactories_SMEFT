#!/usr/bin/env python3
"""
P_decay for every (operator, MX, final state) from the LHE files of the
production runs, using the X momentum in each event (beta*gamma = p_X / m_X).

  per X:     P_i = exp(-l_inner / (bg*ctau)) - exp(-l_outer / (bg*ctau)),  bg = p_X / m_X
  per row:   P_decay = mean over events of P_i      (events are unweighted)
  ctau [m] = HBAR_C / Gamma_X [GeV]

Event folders are named like the result files, minus '_results.txt':
  cdhielx_ppZXvlvl_BSMEFT_15   -> operator cdhielx, tag ppZXvlvl, MX = 15
and hold  <folder>/Events/run_*/unweighted_events.lhe.gz
"""
import glob
import os

import numpy as np

# ------------------------------ CONFIG ------------------------------
HBAR_C = 1.973269804e-16          # GeV*m
L_INNER, L_OUTER = 0.0, 0.3       # m
PID_X = 9000002

# Z-peak veto for the direct (ppX...) events: the final state is X + 2 fermions, so the
# invariant mass of all outgoing particles is m(X f f). Events with |m - MZ| < N*GammaZ
# are dropped before P_decay is computed. N = 15 matches MadGraph's default bw_cutoff,
# i.e. the region that the resonant (ppZX...) samples cover.
MZ_GEV = 91.188
GAMMA_Z_GEV = 2.441404
Z_VETO_NWIDTHS = 15.0

# folder tag -> final-state label
# Event folders used for P_decay: exactly <operator>_<tag>_BSMEFT_<MX>, nothing after.
RES_EVENT_TAGS = {"ppZXll": "ll", "ppZXvlvl": "vlvl", "ppZXqq": "qq"}   # pp > z, z > x ...  (resonant rows)
DIR_EVENT_TAGS = {"ppXll": "ll", "ppXvlvl": "vlvl", "ppXqq": "qq"}     # pp > x ...        (direct rows)

# X width: result files of the X-decay runs, <op>_<tag>_..._<MX>_results.txt
# (cross column = Gamma_X in GeV; last data row is used). The tags are tried in
# this order and the first one that exists for the operator and mass is used;
# the file that was used is printed. The file must be named exactly
# <op>_<tag>_BSMEFT_<MX>_results.txt, e.g. cXe_XZll_BSMEFT_15_results.txt.
# Both the results folder and the events folder are searched.
# NB: ZXll / ZXvlvl / ZXqq files hold Gamma(Z -> X + ...) (used for the BR), not
# Gamma_X. Only add those tags here if those files really contain the X width.
XWIDTH_TAGS = ["XZll", "XZvlvl", "XZqq"]
XWIDTH_BY_FS = {"ll": "XZll", "vlvl": "XZvlvl", "qq": "XZqq"}   # tried first for a row of that final state
XWIDTH_TAG = XWIDTH_TAGS[0]   # kept for imports
LAMBDA_FILE_GEV = 10000.0   # Lambda the X-width files were generated at
LAMBDA_BENCH_GEV = 10000.0  # Lambda of your tables; Gamma_X is rescaled by (LAMBDA_FILE/LAMBDA_BENCH)**4
GAMMA_X_OVERRIDE = {}       # optional: {(operator, MX): Gamma_X in GeV}, takes precedence over files
# --------------------------------------------------------------------


def run_path_safe(paths):
    return paths[0] if paths else "."


def collect_X_kinematics(paths, pid=PID_X, cache=None):
    """Parse LHE once (cached to .npz); return per-X arrays plus per-event X multiplicity."""
    if cache and os.path.exists(cache):
        cached = dict(np.load(cache))
        if "m_sys" in cached:          # old caches without m_sys are re-parsed
            return cached
    import lhefunctions                      # your module
    try:
        from tqdm import tqdm
    except ImportError:
        tqdm = lambda x, **k: x
    out = {k: [] for k in ["px", "py", "pz", "E", "m_lhe", "m_sys", "nX"]}
    for run_path in tqdm(paths, desc=os.path.basename(os.path.dirname(os.path.dirname(run_path_safe(paths))))):
        lhe_file = f"{run_path}/unweighted_events.lhe.gz"
        if not os.path.exists(lhe_file):
            continue
        for event in lhefunctions.read_lhe_outgoing(lhe_file):
            nX = 0
            # invariant mass of ALL outgoing particles of the event
            tot = np.zeros(4)
            for p in event:
                tot += [p.get("E", p.get("e", p.get("energy", np.nan))), p["px"], p["py"], p["pz"]]
            m_sys = float(np.sqrt(max(tot[0] ** 2 - tot[1] ** 2 - tot[2] ** 2 - tot[3] ** 2, 0.0)))
            for p in event:
                if abs(p["pid"]) != pid:
                    continue
                nX += 1
                out["m_sys"].append(m_sys)
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


def pdecay_from_kin(kin, ctau_scan, mx, l_inner=L_INNER, l_outer=L_OUTER):
    bg = kin["p"] / mx
    res = []
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        for ctau in ctau_scan:
            L = bg * ctau
            P = np.exp(-l_inner / L) * (-np.expm1(-(l_outer - l_inner) / L))
            res.append(np.nanmean(P))
    return np.array(res)


def _last_row_cross(path):
    val = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                val = float(line.split()[2])
    return val


def get_gamma_x(dirs, op, mass, fs=None):
    """Return (Gamma_X in GeV at the benchmark Lambda, file used), or (None, None).

    Only files named exactly <op>_<tag>_BSMEFT_<MX>_results.txt are used
    (tag from XWIDTH_TAGS); lamscan / lamscan2 / ... files are never matched.
    """
    if (op, mass) in GAMMA_X_OVERRIDE:
        return GAMMA_X_OVERRIDE[(op, mass)], "override"
    first = XWIDTH_BY_FS.get(fs)
    tags = ([first] if first else []) + [t for t in XWIDTH_TAGS if t != first]
    for tag in tags:
        name = f"{op}_{tag}_BSMEFT_{mass:g}_results.txt"
        for d in dirs:
            path = os.path.join(d, name)
            if not os.path.exists(path):
                continue
            g = _last_row_cross(path)
            if g is None:
                continue
            return g * (LAMBDA_FILE_GEV / LAMBDA_BENCH_GEV) ** 4, os.path.relpath(path)
    return None, None


def compute_pdecay(events_root, results_root=None, needed=None):
    """Return {(operator, MX, final_state): {'res': P or None, 'dir': P or None}}.

    events_root : folder holding the event folders (<op>_<tag>_BSMEFT_<MX>/Events/run_*)
    results_root: folder holding the *_results.txt files (X-width files); defaults to events_root
    needed      : set of (operator, MX, final_state); only these are processed (None = all)

    Only folders named exactly <op>_<tag>_BSMEFT_<MX> are used (4 parts), so scan
    folders like <op>_<tag>_BSMEFT_lamscan2_<MX> are never picked up.
    """
    root = os.path.expanduser(events_root)
    results_root = os.path.expanduser(results_root) if results_root else root
    width_dirs = list(dict.fromkeys([results_root, root]))
    reported = set()
    out = {}
    print(f"[Pdecay] Gamma_X rescaled from Lambda={LAMBDA_FILE_GEV:g} to {LAMBDA_BENCH_GEV:g} GeV; "
          f"detector l_inner={L_INNER:g} m, l_outer={L_OUTER:g} m")
    for folder in sorted(glob.glob(os.path.join(root, "*"))):
        if not os.path.isdir(folder):
            continue
        parts = os.path.basename(folder).split("_")
        if len(parts) != 4 or parts[2] != "BSMEFT":
            continue
        op, tag = parts[0], parts[1]
        if tag in RES_EVENT_TAGS:
            kind, fs = "res", RES_EVENT_TAGS[tag]
        elif tag in DIR_EVENT_TAGS:
            kind, fs = "dir", DIR_EVENT_TAGS[tag]
        else:
            continue
        try:
            mass = float(parts[-1])
        except ValueError:
            continue
        if needed is not None and (op, mass, fs) not in needed:
            continue
        runs = sorted(glob.glob(os.path.join(folder, "Events", "run_*")))
        if not runs:
            print(f"[Pdecay] {os.path.basename(folder)}: no Events/run_* found; skipped")
            continue
        gam, wfile = get_gamma_x(width_dirs, op, mass, fs)
        if gam is None:
            if (op, mass) not in reported:
                reported.add((op, mass))
                have = sorted({os.path.basename(f) for d in width_dirs
                               for f in glob.glob(os.path.join(d, f"{op}_*_{mass:g}_results.txt"))})
                print(f"[Pdecay] {op} MX={mass:g}: no X-width file with tags {XWIDTH_TAGS} "
                      f"in {width_dirs}; files for this operator and mass: {have[:4] if have else 'none'}")
            continue
        if (op, mass, fs) not in reported:
            reported.add((op, mass, fs))
            print(f"[Pdecay] {op} MX={mass:g} {fs}: Gamma_X = {gam:.3e} GeV from {wfile}")
        ctau = HBAR_C / gam if gam > 0 else float("inf")

        kin = collect_X_kinematics(runs, cache=os.path.join(folder, "X_kin_cache.npz"))
        if kin["p"].size == 0:
            print(f"[Pdecay] {os.path.basename(folder)}: no X found (pid {PID_X}); skipped")
            continue
        m_mean = float(np.nanmean(kin["m_calc"]))
        if abs(m_mean - mass) > 0.5:
            print(f"[warn] {os.path.basename(folder)}: mean X mass in LHE is {m_mean:.2f} GeV, folder says {mass:g}")

        in_win = np.abs(kin["m_sys"] - MZ_GEV) < Z_VETO_NWIDTHS * GAMMA_Z_GEV
        frac_in = float(np.mean(in_win))
        sel = kin
        veto_note = f"in Z window: {frac_in:.3f}"
        if kind == "dir":
            keep = ~in_win
            if not keep.any():
                print(f"[Pdecay] {os.path.basename(folder)}: every X is inside the Z window; skipped")
                continue
            sel = {k: v[keep] for k, v in kin.items() if k != "nX" and v.shape == keep.shape}
            veto_note += f" -> {int(keep.sum())} X kept after Z veto"
        P = float(pdecay_from_kin(sel, [ctau], mass)[0])
        out.setdefault((op, mass, fs), {"res": None, "dir": None})[kind] = P
        print(f"[Pdecay] {folder}\n         {op} MX={mass:g} {fs} {kind}: {kin['p'].size} X, "
              f"ctau={ctau:.3e} m, <bg>={np.mean(sel['p'] / mass):.2f}, P_decay={P:.4e}\n"
              f"         ({veto_note}; resonant samples should be ~1, direct ones small)")
    return out