#!/usr/bin/env python3
"""
Bar plot of BR(Z -> X + ...) for every operator, built automatically from the
Z-decay width result files <op>_<tag>_BSMEFT_<MX>_results.txt (tags from RES_TAGS
of make_signal_csv.py: ZXll, ZXvlvl, ZXqq, ...), with the LEP invisible-width bound drawn as a dashed tick on the purely invisible bars.

    BR = Gamma(Z -> X + ...) / Gamma_Z        (Gamma = 'cross' column, last row, GeV)

Any other tag that starts with 'ZX' (e.g. ZXX, ZXXg, ZXXX, ZXXXX, ZXXll, ZXXqq) is
included too. Labels come from TAG_LABELS / QQ_TAGS; a tag that is missing there is
still plotted and listed in the log.

Usage:  python plot_resonant_br.py
        python plot_resonant_br.py --dir ./output_folds --mx 15 --out BSMEFT_bounds.png
"""
import argparse
import glob
import os
from collections import Counter

import matplotlib.pyplot as plt

try:                                   # keep the tag list in sync with the CSV script
    from make_signal_csv import RES_TAGS
except Exception:
    RES_TAGS = {"ZXll": "ll", "ZXvlvl": "vlvl", "ZXqq": "qq"}

# ------------------------------ CONFIG ------------------------------
RESULTS_DIR = "./output_folds"
OUT_PNG = "BSMEFT_bounds.png"
MX_PLOT = 15.0                     # GeV; only files with this M_X (last token of the name)

GAMMA_Z = 2.4952                   # GeV, used for BR = Gamma / GAMMA_Z (PDG; your old plot value)
LEP_INV_LIMIT_GEV = 0.0025         # exotic invisible width bound, 2.5 MeV (your value)

LAMBDA_FILE_GEV = 10000.0          # Lambda the width files were generated at
LAMBDA_PLOT_GEV = 10000.0          # Lambda shown in the plot; Gamma is rescaled by (file/plot)**4
C_VALUE = 1

XLIM = (5e-11, 1e-1)
# How the LEP bound is drawn on the invisible bars:
#   "marker": hollow diamond at the bound + dotted leader from the end of the bar (shows the headroom)
#   "ticks" : thin solid tick at the bound, one per invisible bar
#   "line"  : one dashed vertical line across the whole plot
LEP_STYLE = "marker"

# Z-decay tags whose final state is purely invisible (X only): the LEP bound is drawn on these bars
INVISIBLE_TAGS = {"ZXX", "ZXXX", "ZXXXX"}
BR_FLOOR = 1e-19                   # bars below this are hidden (numerical noise, e.g. Z -> X nu nu for C_Xe); 0 = show all
BAR_HEIGHT = 0.85
BASE_COLOR = "#F27121"
# --------------------------------------------------------------------

# operator name -> canonical spelling (file names may use any capitalisation)
OP_ORDER = ["Xe", "Xl", "Xq", "Xd", "Xu",
            "DHieLX", "DHiesLX", "DHidQX", "DHidsQX", "DHiQuX", "DHiQsuX",
            "XHiB", "XHiX", "XB", "XB2", "XW2", "XB3", "XB4",
            "H2X2B", "XH2", "XH3", "XH4",
            "Xfl", "Xfd", "Xfu", "XfQ"]
OP_CANON = {name.lower(): name for name in OP_ORDER}
LEPTONIC = {"Xe", "Xl", "DHieLX", "DHiesLX", "Xfl"}
HADRONIC = {"Xq", "Xd", "Xu", "DHidQX", "DHidsQX", "DHiQuX", "DHiQsuX", "Xfd", "Xfu", "XfQ"}
ALPHA = {"lep": 0.6, "had": 0.5, "other": 0.8}

# Z-decay tag (2nd token of the file name) -> text drawn on the bar.
# Tags that are not listed here are still plotted, with a label built from the tag,
# and are reported in the log.
TAG_LABELS = {
    "ZXll":    r"$Z \rightarrow X \ell \bar{\ell}$",
    "ZXvlvl":  r"$Z \rightarrow X \nu_\ell \bar{\nu}_\ell$",
    "ZXg":     r"$Z \rightarrow X \gamma$",
    "ZXX":     r"$Z \rightarrow X X$",
    "ZXXg":    r"$Z \rightarrow X X \gamma$",
    "ZXXX":    r"$Z \rightarrow X X X$",
    "ZXXXX":   r"$Z \rightarrow X X X X$",
    "ZXXll":   r"$Z \rightarrow X X \ell \bar{\ell}$",
    "ZXXvlvl": r"$Z \rightarrow X X \nu_\ell \bar{\nu}_\ell$",
}
# tags with a quark pair: label is built per operator (d dbar, u ubar, or q qbar)
QQ_TAGS = {"ZXqq": "X", "ZXXqq": "X X"}      # tag -> the X's in the final state
QUARK = {"Xd": "d", "DHidQX": "d", "DHidsQX": "d", "Xfd": "d",
         "Xu": "u", "DHiQuX": "u", "DHiQsuX": "u", "Xfu": "u"}   # everything else: q

# A hadronic operator has no X l l decay: a file tagged ZXll / ZXXll for it holds the quark
# channel, so it is shown (and labelled) as the quark pair. If the operator also has a
# ZXqq / ZXXqq file, the ll one is treated as stale and dropped.
LL_TO_QQ = {"ZXll": "ZXqq", "ZXXll": "ZXXqq"}

# order of the bars inside one operator
TAG_ORDER = ["ZXll", "ZXvlvl", "ZXqq", "ZXg", "ZXX", "ZXXg", "ZXXX", "ZXXXX",
             "ZXXll", "ZXXvlvl", "ZXXqq"]


def read_gamma(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                rows.append(float(line.split()[2]))
    if not rows:
        return None
    if len(rows) > 1:
        print(f"[warn] {os.path.basename(path)} has {len(rows)} rows; using the last one")
    return rows[-1]


def collect(dirpath, mx):
    entries, auto_tags, skipped_zero = [], Counter(), []
    scale = (LAMBDA_FILE_GEV / LAMBDA_PLOT_GEV) ** 4
    for path in sorted(glob.glob(os.path.join(dirpath, "*_results.txt"))):
        parts = os.path.basename(path)[: -len("_results.txt")].split("_")
        if len(parts) != 4 or parts[2] != "BSMEFT":      # exact names only (no lamscan etc.)
            continue
        try:
            if float(parts[3]) != mx:
                continue
        except ValueError:
            continue
        raw_op, tag = parts[0], parts[1]
        if tag in RES_TAGS:
            fs = RES_TAGS[tag]
        elif tag.startswith("ZX"):
            fs = tag[2:]
            auto_tags[tag] += 1
        else:
            continue
        g = read_gamma(path)
        if g is None:
            continue
        g *= scale
        if g <= 0:
            skipped_zero.append(os.path.basename(path))
            continue
        op = OP_CANON.get(raw_op[1:].lower() if raw_op[:1].lower() == "c" else raw_op.lower(), raw_op)
        entries.append({"op": op, "fs": fs, "tag": tag, "br": g / GAMMA_Z})

    def key(e):
        o = OP_ORDER.index(e["op"]) if e["op"] in OP_ORDER else len(OP_ORDER)
        f = TAG_ORDER.index(e["tag"]) if e["tag"] in TAG_ORDER else len(TAG_ORDER)
        return (o, e["op"], f, e["tag"])
    # hadronic operators: relabel / drop 'll' files (see LL_TO_QQ)
    present = {(e["op"], e["tag"]) for e in entries}
    kept, relabelled, dropped = [], [], []
    for e in entries:
        if e["op"] in HADRONIC and e["tag"] in LL_TO_QQ:
            new = LL_TO_QQ[e["tag"]]
            if (e["op"], new) in present:
                dropped.append(f"{e['op']}:{e['tag']}")
                continue
            relabelled.append(f"{e['op']}:{e['tag']}->{new}")
            e["tag"] = new
        kept.append(e)
    entries = kept
    if relabelled:
        print("[note] hadronic operators with only an ll-tagged file, shown as the quark pair: "
              + ", ".join(relabelled))
    if dropped:
        print("[note] dropped ll-tagged files for hadronic operators that also have a qq file: "
              + ", ".join(dropped))
    # numerical-noise floor
    hidden = [f"{e['op']}:{e['tag']}" for e in entries if e["br"] < BR_FLOOR]
    if hidden:
        print(f"[note] hidden {len(hidden)} bars with BR < {BR_FLOOR:g}: " + ", ".join(hidden))
    entries = [e for e in entries if e["br"] >= BR_FLOOR]
    entries.sort(key=key)
    return entries, auto_tags, skipped_zero


def proc_label(e):
    tag = e["tag"]
    if tag in QQ_TAGS:
        q = QUARK.get(e["op"], "q")
        return rf"$Z \rightarrow {QQ_TAGS[tag]} {q} \bar{{{q}}}$"
    if tag in TAG_LABELS:
        return TAG_LABELS[tag]
    return rf"$Z \rightarrow {tag[1:]}$"          # fallback, e.g. ZXabc -> Z -> Xabc


def group_alpha(op):
    return ALPHA["lep"] if op in LEPTONIC else ALPHA["had"] if op in HADRONIC else ALPHA["other"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=RESULTS_DIR)
    ap.add_argument("--mx", type=float, default=MX_PLOT)
    ap.add_argument("--out", default=OUT_PNG)
    ap.add_argument("--lep-style", choices=["marker", "ticks", "line"], default=None)
    ap.add_argument("--no-show", action="store_true")
    args = ap.parse_args()
    global LEP_STYLE
    if args.lep_style:
        LEP_STYLE = args.lep_style

    entries, auto_tags, skipped_zero = collect(os.path.expanduser(args.dir), args.mx)
    if not entries:
        raise SystemExit(f"no <op>_<tag>_BSMEFT_{args.mx:g}_results.txt files with a Z-decay tag in {args.dir}")
    unlabelled = {k: v for k, v in auto_tags.items() if k not in TAG_LABELS and k not in QQ_TAGS}
    if unlabelled:
        print("tags with no entry in TAG_LABELS (labelled from the tag; add them): "
              + ", ".join(f"{t} ({n} files)" for t, n in sorted(unlabelled.items())))
    if skipped_zero:
        print(f"skipped {len(skipped_zero)} files with zero width (cannot be drawn on a log axis): "
              + ", ".join(skipped_zero[:6]) + (" ..." if len(skipped_zero) > 6 else ""))
    print(f"plotting {len(entries)} bars, Gamma_Z = {GAMMA_Z} GeV, "
          f"Lambda {LAMBDA_FILE_GEV:g} -> {LAMBDA_PLOT_GEV:g} GeV")

    fig, ax = plt.subplots(figsize=(8, max(7, 0.27 * len(entries))), dpi=150)
    lo = min(XLIM[0], 0.3 * min(e["br"] for e in entries))
    hi = max(XLIM[1], 3 * max(e["br"] for e in entries))

    # first entry at the top: draw from the bottom up
    y_ticks, y_labels = [], []
    group_start, group_op = None, None
    n = len(entries)
    for i, e in enumerate(reversed(entries)):
        y = float(i)
        ax.barh(y, e["br"], height=BAR_HEIGHT, color=BASE_COLOR,
                alpha=group_alpha(e["op"]), edgecolor="none", zorder=3)
        ax.text(lo * 1.3, y, proc_label(e), va="center", ha="left",
                fontsize=10, color="black", fontstyle="italic", zorder=4)
        if e["tag"] in INVISIBLE_TAGS:        # LEP bound only on the purely invisible decays
            lep = LEP_INV_LIMIT_GEV / GAMMA_Z
            if LEP_STYLE == "marker":
                ax.plot([e["br"], lep], [y, y], color="black", linestyle=":", linewidth=1.0, zorder=4)
                ax.plot([lep], [y], marker="D", markersize=6, markerfacecolor="white",
                        markeredgecolor="black", markeredgewidth=1.3, linestyle="none", zorder=6)
            elif LEP_STYLE == "ticks":
                ax.vlines(x=lep, ymin=y - BAR_HEIGHT / 2, ymax=y + BAR_HEIGHT / 2,
                          colors="black", linestyles="-", linewidth=2.0, zorder=5)
        if e["op"] != group_op:
            if group_op is not None:
                y_ticks.append((group_start + y - 1) / 2)
                y_labels.append(rf"$Q_{{{group_op}}}$")
            group_start, group_op = y, e["op"]
    y_ticks.append((group_start + (n - 1)) / 2)
    y_labels.append(rf"$Q_{{{group_op}}}$")

    if LEP_STYLE == "line" and any(e["tag"] in INVISIBLE_TAGS for e in entries):
        ax.axvline(x=LEP_INV_LIMIT_GEV / GAMMA_Z, color="black", linestyle="--", linewidth=1.5, zorder=5)

    ax.set_xscale("log")
    ax.set_xlim(lo, hi)
    ax.set_ylim(-0.7, n - 0.3)
    ax.set_xlabel(r"$\mathrm{Z\ BR}$", fontsize=14)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels, fontsize=13)
    ax.tick_params(axis="both", which="both", direction="in", top=True, right=True, labelsize=12)
    ax.tick_params(axis="y", which="minor", left=False, right=False)

    ax.text(0.98, 0.02,
            rf"$m_{{\mathrm{{BSM}}}} = {args.mx:g}\ \mathrm{{GeV}},\ "
            rf"\Lambda_{{\mathrm{{NP}}}} = {LAMBDA_PLOT_GEV / 1000:g}\ \mathrm{{TeV}},\ c = {C_VALUE}$",
            transform=ax.transAxes, color="#333333", fontsize=9, ha="right", va="bottom")

    fig.tight_layout()
    fig.savefig(args.out, transparent=True)
    print(f"saved {args.out}")
    if not args.no_show:
        plt.show()


if __name__ == "__main__":
    main()