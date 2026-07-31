import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. DATA SETUP (BSM Final States)
# ==========================================

# We map out explicit Y-coordinates for each sub-bar to allow grouping
# Higher values are at the top of the plot
ZSManyDW = 2.4952
plot_data = [
    # Operator, Process, BR Value, Color Shade (Alpha)
    {"op": r"$Q_{Xe}$", "proc": r"$Z \rightarrow X \ell \bar{\ell}$", "br": (5.453e-07/ZSManyDW),  "alpha": 0.4},
    
    {"op": r"$Q_{Xl}$", "proc": r"$Z \rightarrow X \ell \bar{\ell}$", "br": (5.453e-07/ZSManyDW), "alpha": 0.6},
    {"op": r"$Q_{Xl}$", "proc": r"$Z \rightarrow X \nu_\ell \bar{\nu}_\ell$",   "br": (8.183e-07/ZSManyDW),  "alpha": 0.7},
    
    {"op": r"$Q_{Xq}$", "proc": r"$Z \rightarrow X u \bar{u}$",  "br": (1.633e-06/ZSManyDW),  "alpha": 0.5},
    {"op": r"$Q_{Xq}$", "proc": r"$Z \rightarrow X j j$",  "br": (3.269e-06/ZSManyDW),  "alpha": 0.5},
    {"op": r"$Q_{Xq}$", "proc": r"$Z \rightarrow X d \bar{d}$",  "br": (2.409e-06/ZSManyDW),  "alpha": 0.5},
    
    {"op": r"$Q_{Xd}$", "proc": r"$Z \rightarrow X d \bar{d}$",  "br": (2.409e-06/ZSManyDW),  "alpha": 0.5},
    
    {"op": r"$Q_{Xu}$", "proc": r"$Z \rightarrow X u \bar{u}$",  "br": (1.632e-06/ZSManyDW),  "alpha": 0.5},
    
    {"op": r"$Q_{DHieLX}$",   "proc": r"$Z \rightarrow X \ell \bar{\ell}$", "br": (1.607e-05/ZSManyDW),  "alpha": 0.7},
    
    {"op": r"$Q_{DHiesLX}$", "proc": r"$Z \rightarrow X \ell \bar{\ell}$", "br": (3.677e-06/ZSManyDW),  "alpha": 0.7},
    
    {"op": r"$Q_{DHidQX}$", "proc": r"$Z \rightarrow X d \bar{d}$",  "br": (5.97e-06/ZSManyDW),  "alpha": 0.5},
    
    {"op": r"$Q_{DHidsQX}$", "proc": r"$Z \rightarrow X d \bar{d}$",  "br": (3.246e-05/ZSManyDW),  "alpha": 0.5},
    
    {"op": r"$Q_{DHiQuX}$", "proc": r"$Z \rightarrow X u \bar{u}$",  "br": (4.043e-06/ZSManyDW),  "alpha": 0.5},
    
    {"op": r"$Q_{DHiQsuX}$", "proc": r"$Z \rightarrow X u \bar{u}$",  "br": (2.201e-05/ZSManyDW),  "alpha": 0.5},
    
    {"op": r"$Q_{XHiB}$",   "proc": r"$Z \rightarrow X \gamma$", "br": (0.009479/ZSManyDW) , "alpha": 0.8},
    
    {"op": r"$Q_{XHiX}$",   "proc": r"$Z \rightarrow X X$", "br": (0.01177/ZSManyDW) , "alpha": 0.8},
    
    {"op": r"$Q_{XB2}$",   "proc": r"$Z \rightarrow X X \gamma$", "br": (1.782e-05/ZSManyDW) , "alpha": 0.8},
    
    {"op": r"$Q_{XW2}$",   "proc": r"$Z \rightarrow X X \gamma$", "br": (5.601e-06/ZSManyDW) , "alpha": 0.8},
    
    {"op": r"$Q_{XB3}$",   "proc": r"$Z \rightarrow X X X$", "br": (6.487e-06/ZSManyDW) , "alpha": 0.8},
    
    {"op": r"$Q_{XH3}$",   "proc": r"$Z \rightarrow X X X$", "br": (0.002588/ZSManyDW) , "alpha": 0.8},
    
    {"op": r"$Q_{XH4}$",   "proc": r"$Z \rightarrow X X X$", "br": (0.002588/ZSManyDW) , "alpha": 0.8},
    
    {"op": r"$Q_{Xfl}$",   "proc": r"$Z \rightarrow X X \ell \bar{\ell}$", "br": (1.498e-09/ZSManyDW) , "alpha": 0.8},
    {"op": r"$Q_{Xfl}$",   "proc": r"$Z \rightarrow X X \nu_\ell \bar{\nu}_\ell$", "br": (7.924e-09/ZSManyDW) , "alpha": 0.8},
    
    {"op": r"$Q_{Xfd}$",   "proc": r"$Z \rightarrow X X d \bar{d}$", "br": (5.408e-10/ZSManyDW), "alpha": 0.8},
    
    {"op": r"$Q_{Xfu}$",   "proc": r"$Z \rightarrow X X u \bar{u}$", "br": (1.521e-09/ZSManyDW), "alpha": 0.8},
    
    {"op": r"$Q_{XfQ}$",   "proc": r"$Z \rightarrow X X j j$", "br": (1.867e-08/ZSManyDW), "alpha": 0.8}
]

# Base color (Orange) matching the reference paper
base_orange = "#F27121"
bar_height = 0.85  # Fills the space cleanly

# ==========================================
# 2. PLOT CONFIGURATION & DRAWING
# ==========================================

fig, ax = plt.subplots(figsize=(8, 7), dpi=150)

# Track positions to manually place Y-ticks and Operator labels
y_ticks_positions = []
y_ticks_labels = []

# Loop backwards to render from top-down
current_y = 0
prev_op = None
op_group_start_y = 0
op_counts = 0

for i, entry in enumerate(reversed(plot_data)):
    # Draw the horizontal bar
    ax.barh(current_y, entry["br"], height=bar_height, 
            color=base_orange, alpha=entry["alpha"], edgecolor='none', zorder=3)
    
    # Process text label sitting inside the left edge of the bar
    ax.text(1.3e-8, current_y, entry["proc"], va='center', ha='left', 
            fontsize=10, color='black', fontstyle='italic', zorder=4)
    
    # Optional: Add the black dotted line benchmark if present in your data
    if entry["proc"] == r"$t \rightarrow Sj$":
        ax.vlines(x=5e-4, ymin=current_y - bar_height/2, ymax=current_y + bar_height/2, 
                  colors='black', linestyles=':', linewidth=1.5, zorder=5)

    # Grouping logic for Y-axis operator labels
    if entry["op"] != prev_op:
        if prev_op is not None:
            # Place the label at the center of the previous block group
            y_ticks_positions.append(op_group_start_y + (op_counts - 1) * 0.5)
            y_ticks_labels.append(prev_op)
        op_group_start_y = current_y
        op_counts = 1
        prev_op = entry["op"]
    else:
        op_counts += 1
        
    current_y += 1.0  # Spacing step

# Append the final group label
y_ticks_positions.append(op_group_start_y + (op_counts - 1) * 0.5)
y_ticks_labels.append(prev_op)

# ==========================================
# 3. AXES & STYLING
# ==========================================

# Log scale formatting
ax.set_xscale('log')
ax.set_xlim(5e-11, 1e-1)
ax.set_xlabel(r"$\mathrm{Z\ BR}$", fontsize=14)

# Set the custom y-ticks to map perfectly to the middle of operator blocks
ax.set_yticks(y_ticks_positions)
ax.set_yticklabels(y_ticks_labels, fontsize=13)

# Style tweaks (Inward ticks on all sides, white background layout)
ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
ax.tick_params(axis='y', which='minor', left=False, right=False) # Hide minor Y ticks

# Text label annotation at the bottom right corner
ax.text(0.98, 0.02, r"$m_{\mathrm{BSM}} = 10\ \mathrm{GeV},\ \Lambda_{\mathrm{NP}} = 1\ \mathrm{TeV},\ c = 1$", 
        transform=ax.transAxes, color='#333333', fontsize=9, ha='right', va='bottom')
# Add the experimental bound line at 2.5 MeV (0.0025 GeV)
plt.axvline(x=0.0025/ZSManyDW, color='black', linestyle='--', linewidth=1.5, label=r'LEP $\Gamma_{inv}$ Exotic Limit (95% C.L.)')

# Add a text label or an arrow indicating the excluded region
plt.text(0.00255, plt.gca().get_ylim()[1]*0.7, r'LEP $\Gamma_{Z\rightarrow inv}$', color='black', fontsize=10, fontweight='bold')
fig.savefig('BSMEFT_bounds.png', transparent=True)
plt.tight_layout()
plt.show()