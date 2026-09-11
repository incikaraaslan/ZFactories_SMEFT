import matplotlib.pyplot as plt
import numpy as np

HBAR_C = 1.973269804e-16  # GeV*m

# Your LamX scan data (mX = 10 GeV)
lamX = np.array([1000, 2000, 3000, 5000, 7000, 10000, 12000, 15000, 17000, 20000, 22000, 25000, 27000, 30000])

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


file_path = "./output_folds/cXe_XZll_BSMEFT_lamscan_10_results.txt"
partial_widths, partial_width_errors = read_partial_widths(file_path)


# Total width Gamma_total from MadGraph (If X ONLY decays to l+l-, then Gamma_total = partial_width)
# Replace total_widths with your actual Gamma_total array if X has other decay channels (e.g. qq, vv)

file_path2 = "./output_folds/cXe_Xall_BSMEFT_lamscan_10_3b_yesga_results.txt"
total_widths, total_width_errors = read_partial_widths(file_path2)

file_path3 = "./output_folds/cXe_Xall_BSMEFT_lamscan_10_4b_noga_results.txt"
total_width4b, total_width_error4b = read_partial_widths(file_path3)
# total_widths += total_width4 *1e-1

"""file_path4 = "./output_folds/cXe_ppX_BSMEFT_lamscan_15_results.txt"
cross_secs, cs_errors = read_partial_widths(file_path4)"""

"""file_path_sm = "./ATLAS_ZDff_data.txt"
decaylength, brcs_ATLAS = read_partial_widths(file_path_sm)"""

total_widths += total_width4b
# total_width = 8.038e-13 + 5.611e-13
#1.359e-12 

# Calculate Lifetime c*tau
ctau = HBAR_C / partial_widths  # in meters
# Calculate Branching Ratio
br_dilepton = partial_widths / total_widths


# ============================================================
# PLOT BR vs. c*tau
# ============================================================
plt.figure(figsize=(8, 5))

plt.plot(ctau, br_dilepton, "o-", color="crimson", linewidth=2, label=r"$m_X = 10$ GeV")
# plt.plot(decaylength, brcs_ATLAS, "--", color="black", linewidth=2, label=r"ATLAS Bound")
plt.xscale("log")
plt.yscale("log")
#plt.ylim(0, 1.1)  # BR is between 0 and 1

plt.xlabel(r"Proper Lifetime $c\tau$ [m]")
plt.ylabel(r"$\text{BR}(X \to \ell^+\ell^-\text{any})$")
plt.title(r"Branching Ratio vs. Lifetime ($c_{Xe} = 1.0$)")

plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()