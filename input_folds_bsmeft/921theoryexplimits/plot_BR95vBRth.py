import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.stats import poisson
import lhefunctions
import os
import re
import glob
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

try:
    import pandas as pd
except Exception:
    pd = None

try:
    from mt2 import mt2 as mt2_fn
except Exception:
    mt2_fn = None

HBAR_C = 1.973269804e-16  # GeV*m

# Your LamX scan data (mX = 10 GeV)
lamX = np.array([10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1000, 2000, 3000, 5000, 7000, 10000])


def read_partial_widths(filepath):
    partial_widths = []
    partial_width_errors = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines or header comments
            if not line or line.startswith("#"):
                continue

            fields = line.split()

            # Expecting at least 5 columns (run_name, tag, width/cross, error, n_events)
            if len(fields) >= 5:
                # Column index 2 is the width value (GeV)
                partial_widths.append(float(fields[2]))
                # Column index 3 is the statistical error (GeV)
                partial_width_errors.append(float(fields[3]))
            
            if len(fields) == 2:
                # Column index 0 is the c\tau valuee
                partial_widths.append(float(fields[0]))
                # Column index 1 is the cross section * BR valuee
                partial_width_errors.append(float(fields[1]))
                

    return np.array(partial_widths), np.array(partial_width_errors)




################################### THEORY LIMIT, GET MG BR FOR ALL LAMBDA SCANNED ###################################
# Leptonic Operators: cxe, cxl, cdhielx, cdhieslx
file_path_cxe_15 = "../../output_folds/cXe_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cxe_15, partial_width_errors_cxe_15 = read_partial_widths(file_path_cxe_15)

file_path_cxl_15 = "../../output_folds/cXl_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cxl_15, partial_width_errors_cxl_15 = read_partial_widths(file_path_cxl_15)

file_path_cdhielx_15 = "../../output_folds/cdhielx_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cdhielx_15, partial_width_errors_cdhielx_15 = read_partial_widths(file_path_cdhielx_15)

file_path_cdhieslx_15 = "../../output_folds/cdhieslx_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cdhieslx_15, partial_width_errors_cdhieslx_15 = read_partial_widths(file_path_cdhieslx_15)

# Hadronic Operators: cxe, cxl, cdhielx, cdhieslx
file_path_cxq_15 = "../../output_folds/cXq_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cxq_15, partial_width_errors_cxq_15 = read_partial_widths(file_path_cxq_15)

file_path_cxd_15 = "../../output_folds/cXd_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cxd_15, partial_width_errors_cxd_15 = read_partial_widths(file_path_cxd_15)

file_path_cxu_15 = "../../output_folds/cXu_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cxu_15, partial_width_errors_cxu_15 = read_partial_widths(file_path_cxu_15)

file_path_cdhidqx_15 = "../../output_folds/cdhidqx_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cdhidqx_15, partial_width_errors_cdhidqx_15 = read_partial_widths(file_path_cdhidqx_15)

file_path_cdhidsqx_15 = "../../output_folds/cdhidsqx_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cdhidsqx_15, partial_width_errors_cdhidsqx_15 = read_partial_widths(file_path_cdhidsqx_15)

file_path_cdhiqux_15 = "../../output_folds/cdhiqux_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cdhiqux_15, partial_width_errors_cdhiqux_15 = read_partial_widths(file_path_cdhiqux_15)

file_path_cdhiqsux_15 = "../../output_folds/cdhiqsux_ZXll_BSMEFT_lamscan_15_results.txt"
partial_widths_cdhiqsux_15, partial_width_errors_cdhiqsux_15 = read_partial_widths(file_path_cdhiqsux_15)

# X AXIS: Calculate Lifetime c*tau
ctau_th_cxe_15 = HBAR_C / partial_widths_cxe_15  # in meters
ctau_th_cxl_15 = HBAR_C / partial_widths_cxl_15  # in meters
ctau_th_cdhielx_15 = HBAR_C / partial_widths_cdhielx_15  # in meters
ctau_th_cdhieslx_15 = HBAR_C / partial_widths_cdhieslx_15  # in meters

ctau_th_cxq_15 = HBAR_C / partial_widths_cxq_15  # in meters
ctau_th_cxd_15 = HBAR_C / partial_widths_cxd_15  # in meters
ctau_th_cxu_15 = HBAR_C / partial_widths_cxu_15  # in meters
ctau_th_cdhidqx_15 = HBAR_C / partial_widths_cdhidqx_15  # in meters
ctau_th_cdhidsqx_15 = HBAR_C / partial_widths_cdhidsqx_15  # in meters
ctau_th_cdhiqux_15 = HBAR_C / partial_widths_cdhiqux_15  # in meters
ctau_th_cdhiqsux_15 = HBAR_C / partial_widths_cdhiqsux_15  # in meters

# Y AXIS: BR wrt to Z_tot
partial_width_Z_tot = 2.495 # GeV
br_th_cxe_15 = partial_widths_cxe_15 / partial_width_Z_tot
br_th_cxl_15 = partial_widths_cxl_15 / partial_width_Z_tot
br_th_cdhielx_15 = partial_widths_cdhielx_15 / partial_width_Z_tot
br_th_cdhieslx_15 = partial_widths_cdhieslx_15 / partial_width_Z_tot

br_th_cxq_15 = partial_widths_cxq_15 / partial_width_Z_tot
br_th_cxd_15 = partial_widths_cxd_15 / partial_width_Z_tot
br_th_cxu_15 = partial_widths_cxu_15 / partial_width_Z_tot
br_th_cdhidqx_15 = partial_widths_cdhidqx_15 / partial_width_Z_tot
br_th_cdhidsqx_15 = partial_widths_cdhidsqx_15 / partial_width_Z_tot
br_th_cdhiqux_15 = partial_widths_cdhiqux_15 / partial_width_Z_tot
br_th_cdhiqsux_15 = partial_widths_cdhiqsux_15 / partial_width_Z_tot

################################### EXPERIMENTAL LIMIT, TREAT BR AS A VARIABLE WRT C\TAU ###################################
# X AXIS: For an array of lifetimes c*tau
ctau_scan = np.logspace(-13, 4, 200)  # free c*tau axis in meters
# Y AXIS: to Compare to ATLAS searches, expect zero background events ($B = 0$) and detector observes 0 events ($k = 0$),
events_dir_cxe_15 = "../../output_folds/cXe_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cxl_15 = "../../output_folds/cXl_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhielx_15 = "../../output_folds/cdhielx_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhieslx_15 = "../../output_folds/cdhieslx_ppZXll_BSMEFT_lamscan2_15/Events/"


events_dir_cxq_15 = "../../output_folds/cXq_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cxd_15 = "../../output_folds/cXd_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cxu_15 = "../../output_folds/cXu_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhidqx_15 = "../../output_folds/cdhidqx_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhidsqx_15 = "../../output_folds/cdhidsqx_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhiqux_15 = "../../output_folds/cdhiqux_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhiqsux_15 = "../../output_folds/cdhiqsux_R_ppZXll_BSMEFT_lamscan2_15/Events/"

run_paths_cxe_15 = sorted(
    glob.glob(f"{events_dir_cxe_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cxl_15 = sorted(
    glob.glob(f"{events_dir_cxl_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cdhielx_15 = sorted(
    glob.glob(f"{events_dir_cdhielx_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cdhieslx_15 = sorted(
    glob.glob(f"{events_dir_cdhieslx_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)


run_paths_cxq_15 = sorted(
    glob.glob(f"{events_dir_cxq_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cxd_15 = sorted(
    glob.glob(f"{events_dir_cxd_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)
run_paths_cxu_15 = sorted(
    glob.glob(f"{events_dir_cxu_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cdhidqx_15 = sorted(
    glob.glob(f"{events_dir_cdhidqx_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cdhidsqx_15 = sorted(
    glob.glob(f"{events_dir_cdhidsqx_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cdhiqux_15 = sorted(
    glob.glob(f"{events_dir_cdhiqux_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cdhiqsux_15 = sorted(
    glob.glob(f"{events_dir_cdhiqsux_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)


# Defensive wrapper to prevent RuntimeWarning when paths are empty
def get_pdecay_scan(paths, ctau_scan, mx, l_inner=0, l_outer=0.3):
    if not paths:
        print(f"Warning: No run directories found for mX={mx}. Returning NaNs.")
        return np.full_like(ctau_scan, np.nan)

    all_momenta = []
    for run_path in tqdm(paths):
        lhe_file = f"{run_path}/unweighted_events.lhe.gz"
        if not os.path.exists(lhe_file):
            continue
        events = lhefunctions.read_lhe_outgoing(lhe_file)
        for event in events:
            for p in event:
                if abs(p["pid"]) != 9000002:
                    continue
                momentum = np.sqrt(p["px"] ** 2 + p["py"] ** 2 + p["pz"] ** 2)
                all_momenta.append(momentum)

    if len(all_momenta) == 0:
        print(
            f"Warning: No valid particle events parsed. Check PID and LHE structure."
        )
        return np.full_like(ctau_scan, np.nan)

    all_momenta = np.array(all_momenta)
    beta_gamma = all_momenta / mx
    pdecay_scan = []
    for ctau in ctau_scan:
        decay_lengths = beta_gamma * ctau
        P = np.exp(-l_inner / decay_lengths) - np.exp(-l_outer / decay_lengths)
        pdecay_scan.append(np.mean(P))
    return np.array(pdecay_scan)

# all operators share same ppZXll kinematics for X, so one pdecay_scan suffices
# but if you want per-operator, call separately with each run_paths

cross_15, cross_errors_15 = read_partial_widths("../../output_folds/ppZ_BSMEFT_lamscan_results.txt")
sigma_ppZ = np.mean(cross_15)  # SM cross section, Lambda-independent ~45000 pb

Lumi = 3.0e6  # pb^-1
N95 = -np.log(0.05)

pdecay_cxe = get_pdecay_scan(run_paths_cxe_15, ctau_scan, mx=15)
pdecay_cxl = get_pdecay_scan(run_paths_cxl_15, ctau_scan, mx=15)
pdecay_cdhielx = get_pdecay_scan(run_paths_cdhielx_15, ctau_scan, mx=15)
pdecay_cdhieslx = get_pdecay_scan(run_paths_cdhieslx_15, ctau_scan, mx=15)

pdecay_cxq = get_pdecay_scan(run_paths_cxq_15, ctau_scan, mx=15)
pdecay_cxd = get_pdecay_scan(run_paths_cxd_15, ctau_scan, mx=15)
pdecay_cxu = get_pdecay_scan(run_paths_cxu_15, ctau_scan, mx=15)
pdecay_cdhidqx = get_pdecay_scan(run_paths_cdhidqx_15, ctau_scan, mx=15)
pdecay_cdhidsqx = get_pdecay_scan(run_paths_cdhidsqx_15, ctau_scan, mx=15)
pdecay_cdhiqux = get_pdecay_scan(run_paths_cdhiqux_15, ctau_scan, mx=15)
pdecay_cdhiqsux = get_pdecay_scan(run_paths_cdhiqsux_15, ctau_scan, mx=15)

br95_cxe_15     = N95 / (Lumi * sigma_ppZ * pdecay_cxe)
br95_cxl_15     = N95 / (Lumi * sigma_ppZ * pdecay_cxl)
br95_cdhielx_15 = N95 / (Lumi * sigma_ppZ * pdecay_cdhielx)
br95_cdhieslx_15= N95 / (Lumi * sigma_ppZ * pdecay_cdhieslx)

br95_cxq_15     = N95 / (Lumi * sigma_ppZ * pdecay_cxq)
br95_cxd_15     = N95 / (Lumi * sigma_ppZ * pdecay_cxd)
br95_cxu_15     = N95 / (Lumi * sigma_ppZ * pdecay_cxu)
br95_cdhidqx_15 = N95 / (Lumi * sigma_ppZ * pdecay_cdhidqx)
br95_cdhidsqx_15= N95 / (Lumi * sigma_ppZ * pdecay_cdhidsqx)
br95_cdhiqux_15 = N95 / (Lumi * sigma_ppZ * pdecay_cdhiqux)
br95_cdhiqsux_15= N95 / (Lumi * sigma_ppZ * pdecay_cdhiqsux)
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# PLOT N95/PDecay vs. c*tau
# ============================================================
fig, ax = plt.subplots(figsize=(11, 7))

# Distinct color palettes
colors_lep_ex = ["#003f5c", "#2f4b7c", "#665191", "#a05195"]
colors_lep_th = ["#d45087", "#f95d6a", "#ff7c43", "#ffa600"]

colors_had_ex = [
    "#800000",
    "#9A0000",
    "#B22222",
    "#C73E1D",
    "#E03C31",
    "#EE6055",
    "#FA8072",
]
colors_had_th = [
    "#00441b",
    "#006d2c",
    "#238b45",
    "#41ab5d",
    "#66c2a4",
    "#80cd99",
    "#a6bdbb",
]  # Fixed typo here

# --- 1. Leptonic Experimental Limits (Solid, Circles) ---
(line_cxe,) = ax.plot(
    ctau_scan,
    br95_cxe_15,
    "o-",
    color=colors_lep_ex[0],
    linewidth=2,
    markersize=4,
)
(line_cxl,) = ax.plot(
    ctau_scan,
    br95_cxl_15,
    "o-",
    color=colors_lep_ex[1],
    linewidth=2,
    markersize=4,
)
(line_cdhielx,) = ax.plot(
    ctau_scan,
    br95_cdhielx_15,
    "o-",
    color=colors_lep_ex[2],
    linewidth=2,
    markersize=4,
)
(line_cdhieslx,) = ax.plot(
    ctau_scan,
    br95_cdhieslx_15,
    "o-",
    color=colors_lep_ex[3],
    linewidth=2,
    markersize=4,
)

# --- 2. Hadronic Experimental Limits (Solid, Triangles) ---
(line_cxq,) = ax.plot(
    ctau_scan,
    br95_cxq_15,
    "^-",
    color=colors_had_ex[0],
    linewidth=2,
    markersize=4,
)
(line_cxd,) = ax.plot(
    ctau_scan,
    br95_cxd_15,
    "^-",
    color=colors_had_ex[1],
    linewidth=2,
    markersize=4,
)
(line_cxu,) = ax.plot(
    ctau_scan,
    br95_cxu_15,
    "^-",
    color=colors_had_ex[2],
    linewidth=2,
    markersize=4,
)
(line_cdhidqx,) = ax.plot(
    ctau_scan,
    br95_cdhidqx_15,
    "^-",
    color=colors_had_ex[3],
    linewidth=2,
    markersize=4,
)
(line_cdhidsqx,) = ax.plot(
    ctau_scan,
    br95_cdhidsqx_15,
    "^-",
    color=colors_had_ex[4],
    linewidth=2,
    markersize=4,
)
(line_cdhiqux,) = ax.plot(
    ctau_scan,
    br95_cdhiqux_15,
    "^-",
    color=colors_had_ex[5],
    linewidth=2,
    markersize=4,
)
(line_cdhiqsux,) = ax.plot(
    ctau_scan,
    br95_cdhiqsux_15,
    "^-",
    color=colors_had_ex[6],
    linewidth=2,
    markersize=4,
)

# --- 3. Leptonic Theory Predictions (Dashed, Squares) ---
valid = lamX > 91
(line_cxe_th,) = ax.plot(
    ctau_th_cxe_15[valid],
    br_th_cxe_15[valid],
    "s--",
    color=colors_lep_th[0],
    linewidth=2,
    markersize=4,
)
(line_cxl_th,) = ax.plot(
    ctau_th_cxl_15[valid],
    br_th_cxl_15[valid],
    "s--",
    color=colors_lep_th[1],
    linewidth=2,
    markersize=4,
)
(line_cdhielx_th,) = ax.plot(
    ctau_th_cdhielx_15[valid],
    br_th_cdhielx_15[valid],
    "s--",
    color=colors_lep_th[2],
    linewidth=2,
    markersize=4,
)
(line_cdhieslx_th,) = ax.plot(
    ctau_th_cdhieslx_15[valid],
    br_th_cdhieslx_15[valid],
    "s--",
    color=colors_lep_th[3],
    linewidth=2,
    markersize=4,
)

# --- 4. Hadronic Theory Predictions (Dashed, Diamonds) ---
(line_cxq_th,) = ax.plot(
    ctau_th_cxq_15[valid],
    br_th_cxq_15[valid],
    "d--",
    color=colors_had_th[0],
    linewidth=2,
    markersize=4,
)
(line_cxd_th,) = ax.plot(
    ctau_th_cxd_15[valid],
    br_th_cxd_15[valid],
    "d--",
    color=colors_had_th[1],
    linewidth=2,
    markersize=4,
)
(line_cxu_th,) = ax.plot(
    ctau_th_cxu_15[valid],
    br_th_cxu_15[valid],
    "d--",
    color=colors_had_th[2],
    linewidth=2,
    markersize=4,
)
(line_cdhidqx_th,) = ax.plot(
    ctau_th_cdhidqx_15[valid],
    br_th_cdhidqx_15[valid],
    "d--",
    color=colors_had_th[3],
    linewidth=2,
    markersize=4,
)
(line_cdhidsqx_th,) = ax.plot(
    ctau_th_cdhidsqx_15[valid],
    br_th_cdhidsqx_15[valid],
    "d--",
    color=colors_had_th[4],
    linewidth=2,
    markersize=4,
)
(line_cdhiqux_th,) = ax.plot(
    ctau_th_cdhiqux_15[valid],
    br_th_cdhiqux_15[valid],
    "d--",
    color=colors_had_th[5],
    linewidth=2,
    markersize=4,
)
(line_cdhiqsux_th,) = ax.plot(
    ctau_th_cdhiqsux_15[valid],
    br_th_cdhiqsux_15[valid],
    "d--",
    color=colors_had_th[6],
    linewidth=2,
    markersize=4,
)

# Legend setup
header_leptonic_ex = mpatches.Rectangle(
    (0, 0), 1, 1, fill=False, edgecolor="none", visible=False
)
header_leptonic_th = mpatches.Rectangle(
    (0, 0), 1, 1, fill=False, edgecolor="none", visible=False
)
header_hadronic_ex = mpatches.Rectangle(
    (0, 0), 1, 1, fill=False, edgecolor="none", visible=False
)
header_hadronic_th = mpatches.Rectangle(
    (0, 0), 1, 1, fill=False, edgecolor="none", visible=False
)

handles = [
    header_leptonic_ex,
    line_cxe,
    line_cxl,
    line_cdhielx,
    line_cdhieslx,
    header_leptonic_th,
    line_cxe_th,
    line_cxl_th,
    line_cdhielx_th,
    line_cdhieslx_th,
    header_hadronic_ex,
    line_cxq,
    line_cxd,
    line_cxu,
    line_cdhidqx,
    line_cdhidsqx,
    line_cdhiqux,
    line_cdhiqsux,
    header_hadronic_th,
    line_cxq_th,
    line_cxd_th,
    line_cxu_th,
    line_cdhidqx_th,
    line_cdhidsqx_th,
    line_cdhiqux_th,
    line_cdhiqsux_th,
]

labels = [
    r"$\bf{Leptonic\ Operators\ EXP:}$",
    r"$(cXe)\ m_X = 15$ GeV",
    r"$(cXl)\ m_X = 15$ GeV",
    r"$(cdhielx)\ m_X = 15$ GeV",
    r"$(cdhieslx)\ m_X = 15$ GeV",
    r"$\bf{Leptonic\ Operators\ TH:}$",
    r"$(cXe)\ m_X = 15$ GeV",
    r"$(cXl)\ m_X = 15$ GeV",
    r"$(cdhielx)\ m_X = 15$ GeV",
    r"$(cdhieslx)\ m_X = 15$ GeV",
    r"$\bf{Hadronic\ Operators\ EXP:}$",
    r"$(cxq)\ m_X = 15$ GeV",
    r"$(cxd)\ m_X = 15$ GeV",
    r"$(cxu)\ m_X = 15$ GeV",
    r"$(cdhidqx)\ m_X = 15$ GeV",
    r"$(cdhidsqx)\ m_X = 15$ GeV",
    r"$(cdhiqux)\ m_X = 15$ GeV",
    r"$(cdhiqsux)\ m_X = 15$ GeV",
    r"$\bf{Hadronic\ Operators\ TH:}$",
    r"$(cxq)\ m_X = 15$ GeV",
    r"$(cxd)\ m_X = 15$ GeV",
    r"$(cxu)\ m_X = 15$ GeV",
    r"$(cdhidqx)\ m_X = 15$ GeV",
    r"$(cdhidsqx)\ m_X = 15$ GeV",
    r"$(cdhiqux)\ m_X = 15$ GeV",
    r"$(cdhiqsux)\ m_X = 15$ GeV",
]

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-13, 1e4)
ax.grid(True, which="both", alpha=0.3)

ax.set_xlabel(r"$c\tau$ [m]", fontsize=12)
ax.set_ylabel(
    r"95% CL Upper Limit on $\text{BR}_{Z \rightarrow X \ell^+\ell^-}$",
    fontsize=12,
)
ax.set_title(
    r"95% CL Upper Limit on Branching Ratio vs. Decay Length ($c = 1.0$)",
    fontsize=13,
)

ax.legend(
    handles,
    labels,
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    frameon=True,
    fontsize=8,
    ncol=2,
)

plt.tight_layout()
plt.savefig("plotBR95VBRth.png", dpi=300, bbox_inches="tight")
plt.show()