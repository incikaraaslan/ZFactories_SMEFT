import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. INPUT YOUR DATA HERE
# ==========================================

# X-axis labels (LaTeX formatted)
operators = [
    r"$C_{hWB}$",
    r"$C_{eW}$",
    r"$C_{Hl}^{(1)}$",
    r"$C_{Hq}^{(1)}$",
    r"$C_{Hq}^{(3)}$",
    r"$C_{Hu}$"
]

# Height of the main solid bars (Current Experimental Bounds)
bar_values = [12.9, 7905, 10.54, 10, 10, 5.77]

# --- HL-LHC Projections (Orange) ---
hllhc_lines = np.asarray([1.99, 2.01, 1.91, 2.04, 2.04, 1.97])**2
hllhc_labels = [
    r"$Z\rightarrow l_p \bar{l}_p$", 
    r"$Z\rightarrow l_p \bar{l}_p$", 
    r"$Z\rightarrow l_p \bar{l}_p$", 
    r"$Z\rightarrow q \bar{q}$",
    r"$Z\rightarrow q \bar{q}$",
    r"$Z\rightarrow u \bar{u}$"
]

# --- FCC-hh Projections (Teal) ---
# [!] Swap these placeholders with your actual computed FCC-hh values
fcchh_lines = np.asarray([2.22, 2.25, 2.13, 2.29, 2.29, 2.20])**2  
fcchh_labels = [
    r"$Z\rightarrow l_p \bar{l}_p$", 
    r"$Z\rightarrow l_p \bar{l}_p$", 
    r"$Z\rightarrow l_p \bar{l}_p$", 
    r"$Z\rightarrow q \bar{q}$",
    r"$Z\rightarrow q \bar{q}$",
    r"$Z\rightarrow u \bar{u}$"
]

# ==========================================
# 2. PLOT CONFIGURATION & STYLING
# ==========================================

# Colors
bar_color = "#7D549E"       # Academic Purple
orange_color = "#E05A2B"    # HL-LHC Projection Line
teal_color = "#2B9CA3"      # FCC-hh Projection Line

x = np.arange(len(operators))  # Label locations
width = 0.4                    # Bar width

fig, ax = plt.subplots(figsize=(12, 5), dpi=150)

# --- Plotting the Bars ---
for i in range(len(operators)):
    # 1. Main Solid Purple Bar
    ax.bar(x[i], bar_values[i], width, color=bar_color, edgecolor='none', zorder=2)
    
    # 2. HL-LHC Lines (Extended width on the left)
    ax.hlines(y=hllhc_lines[i], xmin=x[i] - 0.45, xmax=x[i] - 0.05, 
              colors=orange_color, linestyles='--', linewidth=2.0, zorder=4)
    # Label centered above the elongated left segment
    ax.text(x[i] - 0.25, hllhc_lines[i] * 1.3, hllhc_labels[i], 
            color=orange_color, fontsize=9.5, ha='center', va='bottom', zorder=5)
    
    # 3. FCC-hh Lines (Extended width on the right)
    ax.hlines(y=fcchh_lines[i], xmin=x[i] + 0.05, xmax=x[i] + 0.45, 
              colors=teal_color, linestyles='--', linewidth=2.0, zorder=4)
    # Label centered above the elongated right segment
    ax.text(x[i] + 0.25, fcchh_lines[i] * 1.3, fcchh_labels[i], 
            color=teal_color, fontsize=9.5, ha='center', va='bottom', zorder=5)

# --- Benchmarking Labels (Top Right Legend-Style Text) ---
ax.text(0.98, 0.92, r"$\mathrm{HL-LHC}: 14\ \mathrm{TeV},\ 3 \times 10^6\ \mathrm{pb}^{-1}$", 
        transform=ax.transAxes, color=orange_color, fontsize=11, ha='right', va='top')
ax.text(0.98, 0.84, r"$\mathrm{FCC-hh}: 100\ \mathrm{TeV},\ 3 \times 10^6\ \mathrm{pb}^{-1}$", 
        transform=ax.transAxes, color=teal_color, fontsize=11, ha='right', va='top')

# --- Axes Formatting ---
ax.set_yscale('log')
ax.set_ylim(0.1, 2e4)
ax.set_ylabel(r"$\Lambda\ [\mathrm{TeV}]$", fontsize=14)

# X-axis ticks and placement
ax.set_xticks(x)
ax.set_xticklabels(operators, fontsize=13)

# Style tweaks for an inward academic tick look
ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=11)
ax.grid(False)

fig.savefig('SMEFT_bounds.png', transparent=True)
plt.tight_layout()
plt.show()