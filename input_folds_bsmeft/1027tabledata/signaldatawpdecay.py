#!/usr/bin/env python3
"""
Build one CSV of signal cross sections from MadGraph print_results files,
one row per (operator, MX, final state).

For each row:
  1) resonant   : sigma_res    = sigma(pp -> Z) * Gamma(Z -> X + ...) / Gamma_Z
  2) direct     : sigma_nonres = sigma_incl(pp -> X + ...) - sigma_res
  total         : sigma_total  = sigma_res + sigma_nonres   (== sigma_incl)

File name convention:  <operator>_<processtag>_..._<MX>_results.txt
  e.g. cXe_ZXvlvl_BSMEFT_15_results.txt -> operator cXe, tag ZXvlvl, MX = 15
"""
import argparse
import csv
import glob
import math
import os
from collections import defaultdict

from pdecay_block import compute_pdecay, RES_EVENT_TAGS, DIR_EVENT_TAGS, XWIDTH_TAGS   # P_decay from the LHE files

# ------------------------------ CONFIG ------------------------------
RESULTS_DIR = "./output_folds"
PPZ_FILE = "~/ZFactories_SMEFT/output_folds/ppZ_SM_results.txt"
EVENTS_DIR = "~/ZFactories_SMEFT/output_folds"   # where the event folders (LHE files) live
OUT_CSV = "signal_summary.csv"

# Total Z width in GeV. 2.441404 is the MG5 'sm' default WZ; PDG is ~2.4955.
# Use the same value that is in the param card of your pp > z run.
GAMMA_Z = 2.441404

# tag (2nd token of the file name) -> final-state label
RES_TAGS = {               # Z -> X + ... decay runs (partial width in 'cross' column)
    "ZXll": "ll",
    "ZXvlvl": "vlvl",
    "ZXqq": "qq",
    "ZXg": "a",
}
DIRECT_TAGS = {            # inclusive pp -> X + ... runs (cross section in pb)
    "ppXll": "ll",
    "ppXvlvl": "vlvl",
    "ppXqq": "qq",
}

# final states that have no direct-production (ppX...) run: the row is resonant-only,
# the direct columns stay blank and N_total = N_res
RES_ONLY_FS = {"a"}

PB_TO_FB = 1000.0
SIG_DIGITS = 3             # significant digits in the LaTeX numbers
LUMI_FB = 3.0e3            # integrated luminosity in fb^-1 (3 ab^-1, HL-LHC)
EPSILON = 1.0              # trigger/reconstruction efficiency (assumed 1)
# --------------------------------------------------------------------


def read_result(path):
    """Return (value, error) from the last data row of a print_results file."""
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            p = line.split()
            rows.append((float(p[2]), float(p[3])))
    if not rows:
        raise ValueError(f"no data rows in {path}")
    if len(rows) > 1:
        print(f"[warn] {path} has {len(rows)} runs; using the last one")
    return rows[-1]


def tex(x, digits=SIG_DIGITS):
    """Format a number as $m \\times 10^{e}$ (plain $m$ if the exponent is 0)."""
    if x == 0:
        return "$0$"
    m, e = f"{x:.{digits - 1}e}".split("e")
    e = int(e)
    return f"${m}$" if e == 0 else f"${m} \\times 10^{{{e}}}$"


def rel(err, val):
    return err / val if val != 0 else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=RESULTS_DIR)
    ap.add_argument("--ppz", default=PPZ_FILE)
    ap.add_argument("--events", default=EVENTS_DIR)
    ap.add_argument("--out", default=OUT_CSV)
    ap.add_argument("--plain", action="store_true",
                    help="write plain 1.234e-05 numbers instead of LaTeX")
    args = ap.parse_args()
    args.dir = os.path.expanduser(args.dir)
    args.ppz = os.path.expanduser(args.ppz)

    sig_ppz, err_ppz = read_result(args.ppz)  # pb

    res, direct = defaultdict(dict), defaultdict(dict)  # (op, MX) -> {final state: (val, err)}
    for path in sorted(glob.glob(os.path.join(args.dir, "*_results.txt"))):
        if os.path.abspath(path) == os.path.abspath(args.ppz):
            continue
        stem = os.path.basename(path)[: -len("_results.txt")]
        parts = stem.split("_")
        if len(parts) < 3:
            print(f"[skip] cannot parse name: {path}")
            continue
        op, tag = parts[0], parts[1]
        try:
            mass = float(parts[-1])
        except ValueError:
            print(f"[skip] no mass at end of name: {path}")
            continue
        if tag in RES_TAGS:
            store, fs = res, RES_TAGS[tag]
        elif tag in DIRECT_TAGS:
            store, fs = direct, DIRECT_TAGS[tag]
        elif tag in RES_EVENT_TAGS or tag in DIR_EVENT_TAGS or tag in XWIDTH_TAGS:
            continue   # results of the event-generation runs used for P_decay; not needed here
        else:
            print(f"[skip] unrecognised process tag '{tag}': {path}")
            continue
        if fs in store[(op, mass)]:
            print(f"[warn] {op} MX={mass} {fs}: duplicate file {path}; overwriting earlier one")
        store[(op, mass)][fs] = read_result(path)

    header = [
        "operator", "MX_GeV", "final_state",
        "sigma_ppZ_fb", "Gamma_ZX_GeV", "BR_ZX",
        "sigma_res_fb", "sigma_res_err_fb",
        "sigma_incl_fb", "sigma_incl_err_fb",
        "sigma_nonres_fb", "sigma_nonres_err_fb",
        "sigma_total_fb", "sigma_total_all_fs_fb",
        "Pdecay_res", "Pdecay_direct",
        "N_res", "N_nonres", "N_total", "N_total_all_fs",
    ]

    keys = sorted({(op, mass, fs)
                   for d in (res, direct)
                   for (op, mass), states in d.items()
                   for fs in states})

    out_rows = []
    for op, mass, fs in keys:
        if fs not in res.get((op, mass), {}):
            print(f"[warn] {op} MX={mass} {fs}: missing Z-decay file; row skipped")
            continue
        has_direct = fs in direct.get((op, mass), {})
        if not has_direct and fs not in RES_ONLY_FS:
            print(f"[warn] {op} MX={mass} {fs}: missing direct-production file; row skipped")
            continue

        gam, err_gam = res[(op, mass)][fs]

        br = gam / GAMMA_Z
        s_res = sig_ppz * br * PB_TO_FB
        e_res = s_res * math.hypot(rel(err_ppz, sig_ppz), rel(err_gam, gam))

        if has_direct:
            s_incl_pb, e_incl_pb = direct[(op, mass)][fs]
            s_incl = s_incl_pb * PB_TO_FB
            e_incl = e_incl_pb * PB_TO_FB

            s_non = s_incl - s_res
            e_non = math.hypot(e_incl, e_res)
            if s_non < 0:
                print(f"[warn] {op} MX={mass} {fs}: non-resonant sigma is negative "
                      f"({s_non:.3e} fb); check the inputs or MC noise")
            s_tot = s_res + s_non
        else:
            s_incl = e_incl = s_non = e_non = None
            s_tot = s_res          # resonant only
        out_rows.append([
            op, mass, fs,
            sig_ppz * PB_TO_FB, gam, br,
            s_res, e_res, s_incl, e_incl, s_non, e_non, s_tot,
        ])

    # P_decay only for the (operator, MX, final state) rows that are in the CSV
    needed = {(r[0], r[1], r[2]) for r in out_rows}
    pdec = compute_pdecay(args.events, args.dir, needed)   # {(op, MX, fs): {'res': P, 'dir': P}}

    # sum sigma_total over all final states of the same (operator, MX)
    totals = defaultdict(float)
    for r in out_rows:
        totals[(r[0], r[1])] += r[12]
    for r in out_rows:
        r.append(totals[(r[0], r[1])])
        p = pdec.get((r[0], r[1], r[2]), {})
        r.append(p.get("res"))
        r.append(p.get("dir"))

    # N_events = L * sigma * P_decay * epsilon, with P_decay from the matching events
    n_all = defaultdict(float)
    for r in out_rows:
        s_res_fb, s_non_fb, p_res, p_dir = r[6], r[10], r[14], r[15]
        n_res = LUMI_FB * EPSILON * s_res_fb * p_res if p_res is not None else None
        n_non = (LUMI_FB * EPSILON * s_non_fb * p_dir
                 if (p_dir is not None and s_non_fb is not None) else None)
        if r[2] in RES_ONLY_FS:
            n_tot = n_res          # no direct-production run for this final state
        else:
            n_tot = n_res + n_non if (n_res is not None and n_non is not None) else None
        if n_tot is not None:
            n_all[(r[0], r[1])] += n_tot
        r += [n_res, n_non, n_tot]
    for r in out_rows:
        r.append(n_all.get((r[0], r[1])))

    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in out_rows:
            fmt = (lambda x: f"{x:.6e}") if args.plain else tex
            w.writerow([r[0], r[1], r[2]] + ["" if x is None else fmt(x) for x in r[3:]])

    print("note: Pdecay_direct uses the ppX... events with the Z window vetoed (see pdecay_block.py)")
    print(f"wrote {len(out_rows)} rows to {args.out}")


if __name__ == "__main__":
    main()