import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.stats import poisson
import lhefunctions
import gzip
import os
import re
import glob
from tqdm import tqdm
from scipy.interpolate import CubicSpline

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


file_path_cxe_10 = "./output_folds/cXe_XZll_BSMEFT_lamscan2_10_results.txt"
partial_widths_cxe_10, partial_width_errors_cxe_10 = read_partial_widths(file_path_cxe_10)

file_path_cxe_15 = "./output_folds/cXe_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cxe_15, partial_width_errors_cxe_15 = read_partial_widths(file_path_cxe_15)

file_path_cxe_200 = "./output_folds/cXe_XZll_BSMEFT_lamscan2_200_results.txt"
partial_widths_cxe_200, partial_width_errors_cxe_200 = read_partial_widths(file_path_cxe_200)

file_path_cxl_15 = "./output_folds/cXl_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cxl_15, partial_width_errors_cxl_15 = read_partial_widths(file_path_cxl_15)

file_path_cdhielx_15 = "./output_folds/cdhielx_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cdhielx_15, partial_width_errors_cdhielx_15 = read_partial_widths(file_path_cdhielx_15)

file_path_cdhieslx_15 = "./output_folds/cdhieslx_XZll_BSMEFT_lamscan2_15_results.txt"
partial_widths_cdhieslx_15, partial_width_errors_cdhieslx_15 = read_partial_widths(file_path_cdhieslx_15)

# X AXIS: Calculate Lifetime c*tau
ctau_cxe_10 = HBAR_C / partial_widths_cxe_10  # in meters
ctau_cxe_15 = HBAR_C / partial_widths_cxe_15  # in meters
ctau_cxe_200 = HBAR_C / partial_widths_cxe_200  # in meters
ctau_cxl_15 = HBAR_C / partial_widths_cxl_15  # in meters
ctau_cdhielx_15 = HBAR_C / partial_widths_cdhielx_15  # in meters
ctau_cdhieslx_15 = HBAR_C / partial_widths_cdhieslx_15  # in meters

# Y AXIS: to Compare to ATLAS searches, expect zero background events ($B = 0$) and detector observes 0 events ($k = 0$),

events_dir_cxe_10 = "./output_folds/cXe_ppZXll_BSMEFT_lamscan2_10/Events/"
events_dir_cxe_15 = "./output_folds/cXe_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cxe_200 = "./output_folds/cXe_ppZXll_BSMEFT_lamscan2_200/Events/"
events_dir_cxl_15 = "./output_folds/cXl_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhielx_15 = "./output_folds/cdhielx_ppZXll_BSMEFT_lamscan2_15/Events/"
events_dir_cdhieslx_15 = "./output_folds/cdhieslx_ppZXll_BSMEFT_lamscan2_15/Events/"

run_paths_cxe_10 = sorted(
    glob.glob(f"{events_dir_cxe_10}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cxe_15 = sorted(
    glob.glob(f"{events_dir_cxe_15}/run_*"),
    key=lambda x: int(os.path.basename(x).split("_")[-1])
)

run_paths_cxe_200 = sorted(
    glob.glob(f"{events_dir_cxe_200}/run_*"),
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


p_max_list_cxe_10 = []
p_avg_list_cxe_10 = []
p_max_list_cxe_15 = []
p_avg_list_cxe_15 = []
p_max_list_cxe_200 = []
p_avg_list_cxe_200 = []
p_max_list_cxl_15 = []
p_avg_list_cxl_15 = []
p_max_list_cdhielx_15 = []
p_avg_list_cdhielx_15 = []
p_max_list_cdhieslx_15 = []
p_avg_list_cdhieslx_15 = []

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

"""
def get_cbr(averages, ctau):
    N95 = -np.log(0.05) # Signal such that the probability of observing something even more extreme 
                    # (or in this case, observing 0 events when $S_{95}$ signal events were actually present) is at most 5% 
                    # ($\alpha = 1 - 0.95 = 0.05$).
    mx = 10 # GeV
    # ATLAS Inner Tracker Specs for getting displaced leptons in m
    l_inner = 1e-4
    l_outer = 0.3
    
    beta_gamma = np.asarray(averages) / mx
    z_mean = beta_gamma * ctau
    PDecay = np.exp(-l_inner/z_mean) - np.exp(-l_outer/z_mean)
    cbr95 = N95 / PDecay
    print(PDecay, cbr95)
    return cbr95
"""

cross_cxe_10, cross_errors_cxe_10 = read_partial_widths("./output_folds/cXe_ppZXll_BSMEFT_lamscan2_10_results.txt")
cross_cxe_15, cross_errors_cxe_15 = read_partial_widths("./output_folds/cXe_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cxe_200, cross_errors_cxe_200 = read_partial_widths("./output_folds/cXe_ppZXll_BSMEFT_lamscan2_200_results.txt")
cross_cxl_15, cross_errors_cxl_15 = read_partial_widths("./output_folds/cXl_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cdhielx_15, cross_errors_cdhielx_15 = read_partial_widths("./output_folds/cdhielx_ppZXll_BSMEFT_lamscan2_15_results.txt")
cross_cdhieslx_15, cross_errors_cdhieslx_15 = read_partial_widths("./output_folds/cdhieslx_ppZXll_BSMEFT_lamscan2_15_results.txt")

Lumi = 3.0e6  # pb^-1
N95 = -np.log(0.05)
cbr95_cxe_10 = N95/ (Lumi * get_pdecay(run_paths_cxe_10, ctau_cxe_10, mx=10))
cbr95_cxe_15 = N95/ (Lumi * get_pdecay(run_paths_cxe_15, ctau_cxe_15, mx=15))
cbr95_cxe_200 = N95/ (Lumi * get_pdecay(run_paths_cxe_200, ctau_cxe_200, mx=200))
cbr95_cxl_15 = N95/ (Lumi * get_pdecay(run_paths_cxl_15,  ctau_cxl_15, mx=15))
cbr95_cdhielx_15 = N95/ (Lumi * get_pdecay(run_paths_cdhielx_15,  ctau_cdhielx_15, mx=15))
cbr95_cdhieslx_15= N95/ (Lumi * get_pdecay(run_paths_cdhieslx_15,  ctau_cdhieslx_15, mx=15))


# cbr95_cxe_10 = get_cbr(p_avg_list_cxe_10, ctau_cxe_10)
# cbr95_cxe_15 = get_cbr(p_avg_list_cxe_15, ctau_cxe_15)
# cbr95_cxe_200 = get_cbr(p_avg_list_cxe_200, ctau_cxe_200)
# cbr95_cxl_15 = get_cbr(p_avg_list_cxl_15, ctau_cxl_15)
# cbr95_cdhielx_15 = get_cbr(p_avg_list_cdhielx_15, ctau_cdhielx_15)
# cbr95_cdhieslx_15 = get_cbr(p_avg_list_cdhieslx_15, ctau_cdhieslx_15)

br95_cxe_10 =cbr95_cxe_10/ cross_cxe_10
br95_cxe_15 =cbr95_cxe_15/ cross_cxe_15
br95_cxe_200 =cbr95_cxe_200/ cross_cxe_200
br95_cxl_15 =cbr95_cxl_15/ cross_cxl_15
br95_cdhielx_15  =cbr95_cdhielx_15 / cross_cdhielx_15
br95_cdhieslx_15 =cbr95_cdhieslx_15/ cross_cdhieslx_15

# Compare to ATLAS
file_path_exot = "./ATLASEXOT-2022-17_ZDff_data.txt"
decaylength_EXOT, brcs_ATLAS_EXOT = read_partial_widths(file_path_exot)

file_path_cern = "./ATLASCERN-EP-2025-293_ZDff_data.txt"
decaylength_cern, brcs_ATLAS_CERN = read_partial_widths(file_path_cern)


# ============================================================
# PLOT N95/PDecay vs. c*tau
# ============================================================
plt.figure(figsize=(8, 5))

plt.plot(ctau_cxe_10, br95_cxe_10, "o-", color="crimson", linewidth=2, label=r"$(cXe) m_X = 10$ GeV")
plt.plot(ctau_cxe_15, br95_cxe_15, "o-", color="purple", linewidth=2, label=r"$(cXe) m_X = 15$ GeV")
plt.plot(ctau_cxe_200, br95_cxe_200, "o-", color="green", linewidth=2, label=r"$(cXe) m_X = 200$ GeV")
plt.plot(ctau_cxl_15, br95_cxl_15, "o-", color="blue", linewidth=2, label=r"$(cXl) m_X = 15$ GeV")
plt.plot(ctau_cdhielx_15, br95_cdhielx_15, "o-", color="magenta", linewidth=2, label=r"$(cdhielx) m_X = 15$ GeV")
plt.plot(ctau_cdhieslx_15, br95_cdhieslx_15, "o-", color="pink", linewidth=2, label=r"$(cdhieslx) m_X = 15$ GeV")

plt.xscale("log")
plt.yscale("log")

# Get the top of the actual plot
plt.ylim()

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
plt.xscale("log")
plt.yscale("log")
plt.xlim(1e-10,1e5)
plt.ylim(1e-7,1e8)
plt.grid(
    True,
    which="both",
    alpha=0.3
)

plt.xlabel(r"Proper Lifetime $c\tau$ [m]")
plt.ylabel(r"95% CL Upper Limit on $\text{BR}_{X \rightarrow Z^*l^+l^- \rightarrow f^+f^-l^+l^-}$") #\sigma \times 
plt.title(r"Branching Ratio vs. Lifetime ($c = 1.0$)")

plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()