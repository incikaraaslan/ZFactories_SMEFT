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

# Leptonic Operators: cxe, cxl, cdhielx, cdhieslx

file_path_cxe_15 = "./output_folds/cXe_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cxe_15, partial_width_errors_cxe_15 = read_partial_widths(file_path_cxe_15)

file_path_cxl_15 = "./output_folds/cXl_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cxl_15, partial_width_errors_cxl_15 = read_partial_widths(file_path_cxl_15)

file_path_cdhielx_15 = "./output_folds/cdhielx_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cdhielx_15, partial_width_errors_cdhielx_15 = read_partial_widths(file_path_cdhielx_15)

file_path_cdhieslx_15 = "./output_folds/cdhieslx_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cdhieslx_15, partial_width_errors_cdhieslx_15 = read_partial_widths(file_path_cdhieslx_15)

# Quark Operators: cxq, cxd, cxu, cdhidqx, cdhidsqx, cdhiuqx, cdhiduqx
# RESONANT PRODUCTION
file_path_cxq_15 = "./output_folds/cXq_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cxq_15, partial_width_errors_cxq_15 = read_partial_widths(file_path_cxq_15)

file_path_cxd_15 = "./output_folds/cXd_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cxd_15, partial_width_errors_cxd_15 = read_partial_widths(file_path_cxd_15)

file_path_cxu_15 = "./output_folds/cXu_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cxu_15, partial_width_errors_cxu_15 = read_partial_widths(file_path_cxu_15)

file_path_cdhidqx_15 = "./output_folds/cdhidqx_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cdhidqx_15, partial_width_errors_cdhidqx_15 = read_partial_widths(file_path_cdhidqx_15)

file_path_cdhidsqx_15 = "./output_folds/cdhidsqx_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cdhidsqx_15, partial_width_errors_cdhidsqx_15 = read_partial_widths(file_path_cdhidsqx_15)

file_path_cdhiqux_15 = "./output_folds/cdhiqux_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cdhiqux_15, partial_width_errors_cdhiqux_15 = read_partial_widths(file_path_cdhiqux_15)

file_path_cdhiqsux_15 = "./output_folds/cdhiqsux_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cdhiqsux_15, partial_width_errors_cdhiqsux_15 = read_partial_widths(file_path_cdhiqsux_15)

# X AXIS: Calculate Lifetime c*tau
ctau_cxe_15 = HBAR_C / partial_widths_cxe_15  # in meters
ctau_cxl_15 = HBAR_C / partial_widths_cxl_15  # in meters
ctau_cdhielx_15 = HBAR_C / partial_widths_cdhielx_15  # in meters
ctau_cdhieslx_15 = HBAR_C / partial_widths_cdhieslx_15  # in meters

ctau_cxq_15 = HBAR_C / partial_widths_cxq_15  # in meters
ctau_cxd_15 = HBAR_C / partial_widths_cxd_15  # in meters
ctau_cxu_15 = HBAR_C / partial_widths_cxu_15  # in meters
ctau_cdhidqx_15 = HBAR_C / partial_widths_cdhidqx_15  # in meters
ctau_cdhidsqx_15 = HBAR_C / partial_widths_cdhidsqx_15  # in meters
ctau_cdhiqux_15 = HBAR_C / partial_widths_cdhiqux_15  # in meters
ctau_cdhiqsux_15 = HBAR_C / partial_widths_cdhiqsux_15  # in meters

# Y AXIS: to Compare to ATLAS searches, expect zero background events ($B = 0$) and detector observes 0 events ($k = 0$),

events_dir_cxe_10 = "./output_folds/cXe_ppZXll_BSMEFT_lamscan2_10/Events/"
events_dir_cxe_15 = "./output_folds/cXe_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cxe_200 = "./output_folds/cXe_ppZXll_BSMEFT_lamscan2_200/Events/"
events_dir_cxl_15 = "./output_folds/cXl_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhielx_15 = "./output_folds/cdhielx_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhieslx_15 = "./output_folds/cdhieslx_ppZXll_BSMEFT_lamscan2_15/Events/"

events_dir_cxq_15 = "./output_folds/cXq_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cxd_15 = "./output_folds/cXd_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cxu_15 = "./output_folds/cXu_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhidqx_15 = "./output_folds/cdhidqx_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhidsqx_15 = "./output_folds/cdhidsqx_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhiqux_15 = "./output_folds/cdhiqux_R_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhiqsux_15 = "./output_folds/cdhiqsux_R_ppZXll_BSMEFT_lamscan2_15/Events/"

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


p_max_list_cxe_15 = []
p_avg_list_cxe_15 = []
p_max_list_cxl_15 = []
p_avg_list_cxl_15 = []
p_max_list_cdhielx_15 = []
p_avg_list_cdhielx_15 = []
p_max_list_cdhieslx_15 = []
p_avg_list_cdhieslx_15 = []

p_max_list_cxq_15 = []
p_avg_list_cxq_15 = []
p_max_list_cxd_15 = []
p_avg_list_cxd_15 = []
p_max_list_cxu_15 = []
p_avg_list_cxu_15 = []
p_max_list_cdhidqx_15 = []
p_avg_list_cdhidqx_15 = []
p_max_list_cdhidsqx_15 = []
p_avg_list_cdhidsqx_15 = []
p_max_list_cdhiqux_15 = []
p_avg_list_cdhiqux_15 = []
p_max_list_cdhiqsux_15 = []
p_avg_list_cdhiqsux_15 = []

def get_pavgs(paths, p_max_list_from_distrib, p_avg_list_from_distrib):
    
    for run_path in tqdm(paths):
        run_name = run_path.split("/")[-1]
        lhe_file = f"{run_path}/unweighted_events.lhe.gz"
        events = lhefunctions.read_lhe_outgoing(lhe_file)

        p_components = np.array([
            [p["px"], p["py"], p["pz"]] 
            for event in events 
            for p in event 
            if abs(p["pid"]) == 9000002
        ])

        p_squared_dist = np.sum(p_components**2, axis=1)
        p_max = np.sqrt(np.max(p_squared_dist))
        p_avg = np.sqrt(np.mean(p_squared_dist))
        p_max_list_from_distrib.append(p_max)
        p_avg_list_from_distrib.append(p_avg)
        
def get_pdecay(paths, ctau, mx, l_inner=1e-4, l_outer=0.3):

    pdecay_all = []

    for run_path in tqdm(paths):

        lhe_file = f"{run_path}/unweighted_events.lhe.gz"
        events = lhefunctions.read_lhe_outgoing(lhe_file)

        probs = []

        for event in events:

            for p in event:

                if abs(p["pid"]) != 9000002:
                    continue

                px = p["px"]
                py = p["py"]
                pz = p["pz"]

                momentum = np.sqrt(px**2 + py**2 + pz**2)

                beta_gamma = momentum / mx

                decay_length = beta_gamma * ctau

                P = (
                    np.exp(-l_inner / decay_length)
                    -
                    np.exp(-l_outer / decay_length)
                )

                probs.append(P)

        pdecay_all.append(np.mean(probs))

    return np.asarray(pdecay_all)



cross_cxe_15, cross_errors_cxe_15 = read_partial_widths("./output_folds/cXe_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cxl_15, cross_errors_cxl_15 = read_partial_widths("./output_folds/cXl_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cdhielx_15, cross_errors_cdhielx_15 = read_partial_widths("./output_folds/cdhielx_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cdhieslx_15, cross_errors_cdhieslx_15 = read_partial_widths("./output_folds/cdhieslx_ppZXll_BSMEFT_lamscan2_15_results.txt")

cross_cxq_15, cross_errors_cxq_15 = read_partial_widths("./output_folds/cXq_R_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cxd_15, cross_errors_cxd_15 = read_partial_widths("./output_folds/cXd_R_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cxu_15, cross_errors_cxu_15 = read_partial_widths("./output_folds/cXu_R_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cdhidqx_15, cross_errors_cdhidqx_15 = read_partial_widths("./output_folds/cdhidqx_R_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cdhidsqx_15, cross_errors_cdhidsqx_15 = read_partial_widths("./output_folds/cdhidsqx_R_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cdhiqux_15, cross_errors_cdhiqux_15 = read_partial_widths("./output_folds/cdhiqux_R_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cdhiqsux_15, cross_errors_cdhiqsux_15 = read_partial_widths("./output_folds/cdhiqsux_R_ppZXll_BSMEFT_lamscan2_15_results.txt")

Lumi = 3.0e6  # pb^-1
N95 = -np.log(0.05)
cbr95_cxe_15 = N95/ (Lumi * get_pdecay(run_paths_cxe_15, ctau_cxe_15, mx=15))
cbr95_cxl_15 = N95/ (Lumi * get_pdecay(run_paths_cxl_15,  ctau_cxl_15, mx=15))
cbr95_cdhielx_15 = N95/ (Lumi * get_pdecay(run_paths_cdhielx_15,  ctau_cdhielx_15, mx=15))
cbr95_cdhieslx_15= N95/ (Lumi * get_pdecay(run_paths_cdhieslx_15,  ctau_cdhieslx_15, mx=15))

cbr95_cxq_15 = N95/ (Lumi * get_pdecay(run_paths_cxq_15, ctau_cxq_15, mx=15))
cbr95_cxd_15 = N95/ (Lumi * get_pdecay(run_paths_cxd_15, ctau_cxd_15, mx=15))
cbr95_cxu_15 = N95/ (Lumi * get_pdecay(run_paths_cxu_15, ctau_cxu_15, mx=15))
cbr95_cdhidqx_15 = N95/ (Lumi * get_pdecay(run_paths_cdhidqx_15, ctau_cdhidqx_15, mx=15))
cbr95_cdhidsqx_15 = N95/ (Lumi * get_pdecay(run_paths_cdhidsqx_15, ctau_cdhidsqx_15, mx=15))
cbr95_cdhiqux_15 = N95/ (Lumi * get_pdecay(run_paths_cdhiqux_15, ctau_cdhiqux_15, mx=15))
cbr95_cdhiqsux_15 = N95/ (Lumi * get_pdecay(run_paths_cdhiqsux_15, ctau_cdhiqsux_15, mx=15))

br95_cxe_15 = cbr95_cxe_15/ cross_cxe_15
br95_cxl_15 = cbr95_cxl_15/ cross_cxl_15
br95_cdhielx_15  =cbr95_cdhielx_15 / cross_cdhielx_15
br95_cdhieslx_15 =cbr95_cdhieslx_15/ cross_cdhieslx_15
br95_cdhiqux_15 =cbr95_cdhiqux_15/ cross_cdhiqux_15
br95_cdhiqsux_15 =cbr95_cdhiqsux_15/ cross_cdhiqsux_15

br95_cxq_15 =cbr95_cxq_15/cross_cxq_15
br95_cxd_15 =cbr95_cxd_15/cross_cxd_15
br95_cxu_15 =cbr95_cxu_15/cross_cxu_15
br95_cdhidqx_15 =cbr95_cdhidqx_15/cross_cdhidqx_15
br95_cdhidsqx_15 =cbr95_cdhidsqx_15/cross_cdhidsqx_15
br95_cdhiqux_15 =cbr95_cdhiqux_15/cross_cdhiqux_15
br95_cdhiqsux_15 =cbr95_cdhiqsux_15/cross_cdhiqsux_15

# Compare to ATLAS
"""file_path_exot = "./ATLASEXOT-2022-17_ZDff_data.txt"
decaylength_EXOT, brcs_ATLAS_EXOT = read_partial_widths(file_path_exot)

file_path_cern = "./ATLASCERN-EP-2025-293_ZDff_data.txt"
decaylength_cern, brcs_ATLAS_CERN = read_partial_widths(file_path_cern)"""


# ============================================================
# PLOT N95/PDecay vs. c*tau
# ============================================================
plt.figure(figsize=(8, 5))

header_leptonic = mpatches.Rectangle((0, 0), 1, 1, fill=False, edgecolor='none', visible=False)
header_hadronic = mpatches.Rectangle((0, 0), 1, 1, fill=False, edgecolor='none', visible=False)


line_cxe, = plt.plot(ctau_cxe_15, br95_cxe_15, "o-", color="#800000", linewidth=2, label=r"$(cXe) m_X = 15$ GeV")
line_cxl, = plt.plot(ctau_cxl_15, br95_cxl_15, "o-", color="#B22222", linewidth=2, label=r"$(cXl) m_X = 15$ GeV")
line_cdhielx, = plt.plot(ctau_cdhielx_15, br95_cdhielx_15, "o-", color="#E03C31", linewidth=2, label=r"$(cdhielx) m_X = 15$ GeV")
line_cdhieslx, = plt.plot(ctau_cdhieslx_15, br95_cdhieslx_15, "o-", color="#FA8072", linewidth=2, label=r"$(cdhieslx) m_X = 15$ GeV")

line_cxq, = plt.plot(ctau_cxq_15, br95_cxq_15, "o-", color="#6A0DAD", linewidth=2, label=r"$(cXq) m_X = 15$ GeV")
line_cxd, = plt.plot(ctau_cxd_15, br95_cxd_15, "o-", color="#873DBD", linewidth=2, label=r"$(cXd) m_X = 15$ GeV")
line_cxu, = plt.plot(ctau_cxu_15, br95_cxu_15, "o-", color="#A56DCD", linewidth=2, label=r"$(cXu) m_X = 15$ GeV")
line_cdhidqx, = plt.plot(ctau_cdhidqx_15, br95_cdhidqx_15, "o-", color="#C39EDE", linewidth=2, label=r"$(cdhidqx) m_X = 15$ GeV")
line_cdhidsqx, = plt.plot(ctau_cdhidsqx_15, br95_cdhidsqx_15, "o-", color="#E1CEEE", linewidth=2, label=r"$(cdhidsqx) m_X = 15$ GeV")
line_cdhiqux, = plt.plot(ctau_cdhiqux_15, br95_cdhiqux_15, "o-", color="#4a0979", linewidth=2, label=r"$(cdhiqux) m_X = 15$ GeV")
line_cdhiqsux, = plt.plot(ctau_cdhiqsux_15, br95_cdhiqsux_15, "o-", color="#2a0545", linewidth=2, label=r"$(cdhiqsux) m_X = 15$ GeV")

handles = [
    header_leptonic, line_cxe, line_cxl, line_cdhielx, line_cdhieslx,
    header_hadronic, line_cxq, line_cxd, line_cxu, line_cdhidqx, line_cdhidsqx, line_cdhiqux, line_cdhiqsux
]

labels = [
    r"$\bf{Leptonic\ Operators:}$", r"$(cXe) m_X = 15$ GeV", r"$(cXl) m_X = 15$ GeV", r"$(cdhielx) m_X = 15$ GeV", r"$(cdhieslx) m_X = 15$ GeV",
    r"$\bf{Hadronic\ Operators:}$", r"$(cXq) m_X = 15$ GeV", r"$(cXd) m_X = 15$ GeV", r"$(cXu) m_X = 15$ GeV", r"$(cdhidqx) m_X = 15$ GeV", r"$(cdhidsqx) m_X = 15$ GeV", r"$(cdhiqux) m_X = 15$ GeV", r"$(cdhiqsux) m_X = 15$ GeV"
]

plt.legend(handles, labels, loc='best', frameon=True, fontsize=10)

plt.xscale("log")
plt.yscale("log")


# ============================================================
# ATLAS BOUNDS + SHADED EXCLUDED REGIONS
# ============================================================

# ------------------------------------------------------------
# Black ATLAS bound: EXOT-2022-17
# ------------------------------------------------------------
"""
plt.plot(
    decaylength_EXOT,
    brcs_ATLAS_EXOT,
    "--",
    color="black",
    linewidth=2,
    label=r"ATLAS Bound from EXOT-2022-17 "
        r"(Muon Spec, $m_X = 15$ GeV)"
)

# Make sure the points are sorted in x
sort_exot = np.argsort(decaylength_EXOT)

x_exot = decaylength_EXOT[sort_exot]
y_exot = brcs_ATLAS_EXOT[sort_exot]

# Top of the plotting region
y_top = 1e10

# Shade from the ATLAS curve UP to the top
plt.fill_between(
    x_exot,
    y_exot,
    y_top,
    color="black",
    alpha=0.08,
    zorder=0
)

# Left and right edges
exot_left = x_exot[0]
exot_right = x_exot[-1]

# Starting y-values = actual ATLAS curve endpoints
exot_y_left = y_exot[0]
exot_y_right = y_exot[-1]

# Vertical line starts at the curve and goes upward
plt.plot(
    [exot_left, exot_left],
    [exot_y_left, y_top],
    color="black",
    linestyle=":",
    linewidth=1.5,
    alpha=0.8,
    zorder=1
)

plt.plot(
    [exot_right, exot_right],
    [exot_y_right, y_top],
    color="black",
    linestyle=":",
    linewidth=1.5,
    alpha=0.8,
    zorder=1
)


# ------------------------------------------------------------
# Gray ATLAS bound: CERN-EP-2025-293
# ------------------------------------------------------------

plt.plot(
    decaylength_cern,
    brcs_ATLAS_CERN,
    "--",
    color="grey",
    linewidth=2,
    label=r"ATLAS Bound from CERN-EP-2025-293 "
          r"(Inner Tracker, $m_{Z^{'}} = 200$ GeV)"
)

# Sort the gray bound
sort_cern = np.argsort(decaylength_cern)

x_cern = decaylength_cern[sort_cern]
y_cern = brcs_ATLAS_CERN[sort_cern]

# Shade from the gray ATLAS curve UP to the top
plt.fill_between(
    x_cern,
    y_cern,
    y_top,
    color="grey",
    alpha=0.08,
    zorder=0
)

# Left and right edges
cern_left = x_cern[0]
cern_right = x_cern[-1]

# Starting y-values = actual curve endpoints
cern_y_left = y_cern[0]
cern_y_right = y_cern[-1]

# Vertical lines start at the curve and go upward
plt.plot(
    [cern_left, cern_left],
    [cern_y_left, y_top],
    color="grey",
    linestyle=":",
    linewidth=1.5,
    alpha=0.8,
    zorder=1
)

plt.plot(
    [cern_right, cern_right],
    [cern_y_right, y_top],
    color="grey",
    linestyle=":",
    linewidth=1.5,
    alpha=0.8,
    zorder=1
)
"""

plt.xlim(1e-13,1e4)
plt.ylim(1e-15,1e8)
plt.grid(
    True,
    which="both",
    alpha=0.3
)

plt.xlabel(r"$c\tau$ [m]")
plt.ylabel(r"95% CL Upper Limit on $\text{BR}_{X \rightarrow Z^* f^+f^- \rightarrow f^+f^- f^+f^-}$") 
plt.title(r"95% CL Upper Limit on Branching Ratio vs. Decay Length ($c = 1.0$)")

plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()