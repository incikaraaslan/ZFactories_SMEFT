import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# WIDTHS [GeV]
# ============================================================

partial_widths = {
    "cXe": 5.44e-13,
    "cXl": 4.472e-13,
}

total_widths = {
    "cXe": 6.426e-13,
    "cXl": 6.426e-13,
}

HBAR_C = 1.973269804e-16  # GeV*m


# ============================================================
# CALCULATE BR AND cTAU
# ============================================================

ctau = {}
BR = {}

for op in partial_widths:

    Gamma_partial = partial_widths[op]
    Gamma_total = total_widths[op]

    BR[op] = Gamma_partial / Gamma_total
    ctau[op] = HBAR_C / Gamma_total

    print(
        f"{op}: "
        f"BR = {BR[op]:.6f}, "
        f"c*tau = {ctau[op]:.6e} m"
    )


# ============================================================
# PLOT: BR VS PROPER DECAY LENGTH
# ============================================================

plt.figure(figsize=(8, 6))

for op in BR:

    plt.scatter(
        ctau[op],
        BR[op],
        s=100,
        label=op
    )


plt.xscale("log")

plt.xlabel(r"Proper decay length $c\tau$ [m]")
plt.ylabel(r"Branching ratio $\mathrm{BR}(X\to\ell^+\ell^-+\mathrm{anything})$")

plt.ylim(0, 1.05)

plt.title(r"Leptonic branching ratio vs. $X$ proper decay length")

plt.grid(
    True,
    which="both",
    alpha=0.3
)

plt.legend()

plt.tight_layout()
plt.show()