import json
import matplotlib.pyplot as plt
import numpy as np

# Load data from the automation script
try:
    with open("scan_results.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    # Dummy data fallback for testing before you run the MG5 script
    print("[!] 'scan_results.json' not found. Using dummy verification data.")
    data = {
        "1": {"lambda_min": 1200}, "5": {"lambda_min": 1150}, 
        "10": {"lambda_min": 1050}, "15": {"lambda_min": 980},
        "20": {"lambda_min": 890}, "25": {"lambda_min": 780}, 
        "30": {"lambda_min": 640}, "35": {"lambda_min": 450}, 
        "40": {"lambda_min": 200}
    }

# Extract and sort values
masses = sorted([float(m) for m in data.keys()])
lambdas = [data[str(int(m)) if m.is_integer() else str(m)]["lambda_min"] for m in masses]

# Convert Lambda to TeV for cleaner vertical axes on physics posters
masses = np.array(masses)
lambdas_tev = np.array(lambdas) / 1000.0

# Plot Setup
plt.figure(figsize=(8, 6), dpi=150)
plt.rcParams['text.usetex'] = False  # Set to True if you have working LaTeX on your system
plt.rcParams['font.family'] = 'serif'

# Plot the limit boundary curve
plt.plot(masses, lambdas_tev, color='red', linewidth=2.5, label=r'PDG $Z$-Width Limit Bound')

# Shade the excluded region below the curve
plt.fill_between(masses, lambdas_tev, 0, color='red', alpha=0.15, hatch='//')

# Labels and Text annotations
plt.xlabel(r'Dark Photon Mass $M_X$ [GeV]', fontsize=13, fontweight='bold', labelpad=10)
plt.ylabel(r'EFT Cutoff Scale $\Lambda_{\min}$ [TeV]', fontsize=13, fontweight='bold', labelpad=10)
plt.title(r'Constraints on Vector Singlet EFT from $Z \rightarrow q \bar{q} X X$', fontsize=14, pad=15, fontweight='bold')

# Boundaries and Grid spacing
plt.xlim(min(masses), max(masses))
plt.ylim(0, max(lambdas_tev) * 1.3)
plt.grid(True, which='both', linestyle='--', alpha=0.5)

# Place context labels on the canvas
plt.text(15, max(lambdas_tev) * 0.4, 'EXCLUDED', color='darkred', fontsize=14, fontweight='bold', rotation=-12)
plt.text(20, max(lambdas_tev) * 1.05, 'ALLOWED\nPARAMETER SPACE', color='darkgreen', fontsize=12, fontweight='bold', ha='center')

plt.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none')
plt.tight_layout()

# Save the plot out as a high-res vector file for insertion into LaTeX templates or posters
plt.savefig("EFT_Z_width_exclusion_plot.pdf", format='pdf', bbox_inches='tight')
plt.savefig("EFT_Z_width_exclusion_plot.png", format='png', dpi=300, bbox_inches='tight')
plt.show()