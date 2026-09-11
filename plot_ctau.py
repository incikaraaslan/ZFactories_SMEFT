import os
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# INPUT: Use a dictionary for custom labels!
# Key = Legend Label, Value = File Path
# ============================================================

results_files = {
    r"$c_{Xe}$: X -> l+ l- any": "/home/incik/ZFactories_SMEFT/output_folds/cXe_XZll_BSMEFT_massscan_results.txt",
    r"$c_{Xl}$: X -> l+ l- any": "/home/incik/ZFactories_SMEFT/output_folds/cXl_XZll_BSMEFT_massscan_results.txt",
    r"$c_{DHieLX}$: X -> l+ l- any any": "/home/incik/ZFactories_SMEFT/output_folds/cdhielx_XZll_BSMEFT_massscan_results.txt"
}
"""    r"$c_{DHieLX}$: X -> l+ l- any any": "/home/incik/ZFactories_SMEFT/output_folds/cdhielx_XZll_BSMEFT_massscan_results.txt",
    r"$c_{DHiesLX}$: X -> l+ l- any any": "/home/incik/ZFactories_SMEFT/output_folds/cdhieslx_XZll_BSMEFT_massscan_results.txt","""
# Mass corresponding to each run
masses = np.array([
    10.0,
    12.0,
    15.0,
    20.0,
    25.0,
    30.0,
    40.0,
    50.0,
    60.0,
    70.0,
    80.0,
    90.0,
    100.0,
    150.0,
    200.0,
    250.0,
    300.0,
    350.0,
    400.0,
    450.0,
    500.0,
    550.0,
    600.0,
    650.0,
    700.0,
    1000.0,
    2000.0,
])

# hbar*c in GeV*m
HBAR_C = 1.973269804e-16

# Distinct markers to cycle through automatically
MARKERS = ["o", "s", "^", "v", "D", "P", "X", "*", "h", "<", ">"]


# ============================================================
# HELPER FUNCTIONS
# ============================================================


def read_and_process_results(filepath, expected_masses):
    widths = []
    width_errors = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            fields = line.split()
            if len(fields) < 5:
                continue

            widths.append(float(fields[2]))
            width_errors.append(float(fields[3]))

    widths = np.array(widths)
    width_errors = np.array(width_errors)

    if len(widths) != len(expected_masses):
        raise RuntimeError(
            f"Found {len(widths)} runs in {filepath}, "
            f"but supplied {len(expected_masses)} masses."
        )

    # c*tau = hbar*c / Gamma
    ctau = HBAR_C / widths

    # Uncertainty propagation
    ctau_errors = ctau * width_errors / widths

    return widths, width_errors, ctau, ctau_errors


# ============================================================
# PROCESS DATA & PLOT
# ============================================================

# Handles both dictionary (custom labels) and list (auto labels)
if isinstance(results_files, dict):
    file_items = list(results_files.items())
else:
    file_items = [
        (os.path.basename(path).split("_")[0], path) for path in results_files
    ]

plt.figure(figsize=(9, 6))

for idx, (label, filepath) in enumerate(file_items):
    widths, width_errors, ctau, ctau_errors = read_and_process_results(
        filepath, masses
    )

    # Print Summary Table
    print()
    print("=" * 90)
    print(f"{label} PROPER DECAY LENGTH")
    print("=" * 90)
    print(
        f"{'run':>8}"
        f"{'mX [GeV]':>12}"
        f"{'Gamma [GeV]':>20}"
        f"{'dGamma [GeV]':>20}"
        f"{'c tau [m]':>20}"
        f"{'d(c tau) [m]':>20}"
    )
    print("-" * 90)

    for i in range(len(masses)):
        print(
            f"run_{i+1:02d}"
            f"{masses[i]:12.1f}"
            f"{widths[i]:20.5e}"
            f"{width_errors[i]:20.5e}"
            f"{ctau[i]:20.5e}"
            f"{ctau_errors[i]:20.5e}"
        )

    # Plot Curve using custom label
    marker = MARKERS[idx % len(MARKERS)]
    plt.errorbar(
        ctau,
        masses,
        xerr=ctau_errors,
        fmt=f"{marker}-",
        linewidth=2,
        markersize=6,
        capsize=4,
        label=label,
    )


# ============================================================
# AXES & FORMATTING
# ============================================================

plt.xscale("log")

plt.ylabel(r"$m_X$ [GeV]")
plt.xlabel(r"$c\tau$ [m]")

plt.title(r"$X$ Proper Decay Length vs. $m_X$")

plt.grid(True, which="both", alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()