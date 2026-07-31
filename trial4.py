"""
Invariant mass analysis for SMEFT LHE files.
Python conversion of the Mathematica Chameleon-based routine.

Particles tracked:
  11  : e-
 -12  : anti-nu_e
 -13  : mu+
  14  : nu_mu
"""

import gzip
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# ---- LaTeX Setup for Matplotlib ----
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",  # Uses Computer Modern by default
    "axes.labelsize": 18,
    "font.size": 16,
    "legend.fontsize": 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "text.latex.preamble": r"\usepackage{amsmath}"  # DON'T add newtxtext/newtxmath!
})

# =============================================================
# CONFIG: map PDG IDs to human-readable names
# =============================================================
PARTICLE_NAMES = {
     11: "e-",
    -11: "e+",
     12: "nu_e",
    -12: "anti-nu_e",
     13: "mu-",
    -13: "mu+",
     14: "nu_mu",
    -14: "anti-nu_mu",
     21: "gluon",
      1: "d",     -1: "dbar",
      2: "u",     -2: "ubar",
      5: "b",     -5: "bbar",
      6: "t",     -6: "tbar",
     24: "W+",   -24: "W-",
     23: "Z",
}

# PIDs we care about in this analysis
PARTICLE_IDS = [11, -12, -13, 14]

# =============================================================
# LHE READER
# =============================================================
def open_any(path: str):
    return gzip.open(path, "rt") if path.endswith(".gz") else open(path, "r")


def load_lhe(path: str) -> list:
    """
    Parse an LHE file and return a list of events.
    Each event is a list of particle tuples:
        (pid, status, px, py, pz, E)
    Only final-state particles (status == 1) are kept for analysis,
    but we return all statuses so the caller can filter.
    """
    events = []

    with open_any(path) as f:
        lines = f.readlines()

    i = 0
    n = len(lines)

    while i < n:
        if "<event>" not in lines[i]:
            i += 1
            continue

        i += 1  # skip <event> tag

        # event header line
        header = lines[i].split()
        i += 1

        if not header:
            continue

        try:
            n_particles = int(header[0])
        except ValueError:
            continue

        event = []
        for _ in range(n_particles):
            if i >= n:
                break
            parts = lines[i].split()
            i += 1

            if len(parts) < 10:
                continue

            try:
                pid    = int(parts[0])
                status = int(parts[1])
                px     = float(parts[6])
                py     = float(parts[7])
                pz     = float(parts[8])
                E      = float(parts[9])
                event.append((pid, status, px, py, pz, E))
            except (ValueError, IndexError):
                continue

        events.append(event)

    return events


# =============================================================
# FOUR-VECTOR UTILITIES
# =============================================================
def four_vector(particle: tuple) -> np.ndarray:
    """Return (E, px, py, pz) from a particle tuple."""
    pid, status, px, py, pz, E = particle
    return np.array([E, px, py, pz])


def inv_mass_2(*fvs: np.ndarray) -> float:
    """
    Invariant mass of N four-vectors.
    m^2 = (sum E)^2 - |sum p|^2
    """
    total = sum(fvs)
    m2 = total[0]**2 - np.dot(total[1:], total[1:])
    return np.sqrt(max(m2, 0.0))


# =============================================================
# EXTRACT PARTICLES BY PID FROM ALL EVENTS
# =============================================================
def extract_by_pid(events: list, pid: int, status: int = 1) -> list:
    """
    Return list of four-vectors (E,px,py,pz) for particles
    matching pid and status, one per event.
    Returns None for events where the particle is not found.
    """
    result = []
    for ev in events:
        found = [four_vector(p) for p in ev
                 if p[0] == pid and p[1] == status]
        result.append(found[0] if found else None)
    return result


def build_particle_dict(events: list, pids: list) -> dict:
    """
    Build dict: pid -> list of four-vectors (None if absent in event).
    Mirrors the Mathematica `particles` association.
    """
    return {pid: extract_by_pid(events, pid) for pid in pids}


# =============================================================
# INVARIANT MASS COMPUTATION
# =============================================================
def compute_inv_mass_2body(fv_dict: dict, pid1: int, pid2: int) -> np.ndarray:
    """
    Compute event-by-event invariant mass of two particles.
    Skips events where either particle is missing.
    """
    masses = []
    for fv1, fv2 in zip(fv_dict[pid1], fv_dict[pid2]):
        if fv1 is None or fv2 is None:
            continue
        masses.append(inv_mass_2(fv1, fv2))
    return np.array(masses)


def compute_inv_mass_4body(fv_dict: dict,
                           pid1: int, pid2: int,
                           pid3: int, pid4: int) -> np.ndarray:
    """
    Compute event-by-event invariant mass of four particles.
    Skips events where any particle is missing.
    """
    masses = []
    for fv1, fv2, fv3, fv4 in zip(fv_dict[pid1], fv_dict[pid2],
                                    fv_dict[pid3], fv_dict[pid4]):
        if any(fv is None for fv in [fv1, fv2, fv3, fv4]):
            continue
        masses.append(inv_mass_2(fv1, fv2, fv3, fv4))
    return np.array(masses)


# =============================================================
# LOAD ALL LHE FILES
# =============================================================
FILES = {
    "SMEFTSignal":     "./LHEfiles/QeW_ppvmmvee.lhe",
    "SMEFTSignalQuad": "./LHEfiles/QeW_ppvmmveequad.lhe",
    "SMEFTSignalW":    "./LHEfiles/QeW_ppWvee.lhe",
    "Background":      "./LHEfiles/SMbckg_ZWvee.lhe",
}

print("Loading LHE files...")
events = {}
for label, path in FILES.items():
    try:
        ev = load_lhe(path)
        events[label] = ev
        print(f"  {label}: {len(ev)} events loaded from {path}")
    except FileNotFoundError:
        print(f"  WARNING: {path} not found — skipping {label}")
        events[label] = []

# =============================================================
# BUILD PARTICLE FOUR-VECTOR DICTIONARIES
# =============================================================
# mirrors Mathematica: particles["SMEFTSignal"][-13] etc.
print("\nExtracting particle four-vectors...")
fv = {}  # fv[dataset_label][pid] = list of 4-vectors

for label, ev_list in events.items():
    if ev_list:
        fv[label] = build_particle_dict(ev_list, PARTICLE_IDS)
        for pid in PARTICLE_IDS:
            n_found = sum(1 for v in fv[label][pid] if v is not None)
            print(f"  {label} | PID {pid:4d} ({PARTICLE_NAMES.get(pid,'?'):>10s}): "
                  f"{n_found} / {len(ev_list)} events")
    else:
        fv[label] = {pid: [] for pid in PARTICLE_IDS}

# =============================================================
# INVARIANT MASSES
# =============================================================
print("\nComputing invariant masses...")

# ---- 2-body: mu+ (pid=-13) and e- (pid=11) ----
inv2 = {}
for label in events:
    if events[label]:
        inv2[label] = compute_inv_mass_2body(fv[label], pid1=-13, pid2=11)
        print(f"  M(mu+, e-)   [{label}]: {len(inv2[label])} entries, "
              f"mean = {inv2[label].mean():.1f} GeV" if len(inv2[label]) > 0
              else f"  M(mu+, e-)   [{label}]: 0 entries")

# ---- 4-body: mu+, e-, anti-nu_e, nu_mu ----
inv4 = {}
for label in events:
    if events[label]:
        inv4[label] = compute_inv_mass_4body(
            fv[label], pid1=-13, pid2=11, pid3=-12, pid4=14)
        print(f"  M(all 4 lep) [{label}]: {len(inv4[label])} entries, "
              f"mean = {inv4[label].mean():.1f} GeV" if len(inv4[label]) > 0
              else f"  M(all 4 lep) [{label}]: 0 entries")

# =============================================================
# PLOTTING
# =============================================================

COLORS = {
    "Background":      "#2166ac",
    "SMEFTSignal":     "#d6604d",
    "SMEFTSignalQuad": "#f4a582",
    "SMEFTSignalW":    "#4dac26",
}
LABELS = {
    "Background":      r"SM background ($ZW\nu ee$)",
    "SMEFTSignal":     r"SMEFT $\mathcal{O}_{eW}$ (linear)",
    "SMEFTSignalQuad": r"SMEFT $\mathcal{O}_{eW}$ (quadratic)",
    "SMEFTSignalW":    r"SMEFT $\mathcal{O}_{eW}$ ($W$ only)",
}


def plot_inv_mass(inv_dict: dict, title: str, xlabel: str,
                  bins: np.ndarray, filename: str):
    fig, ax = plt.subplots(figsize=(8, 5))
    for label, masses in inv_dict.items():
        if len(masses) == 0:
            continue
        ax.hist(masses, bins=bins, histtype="step", linewidth=2,
                color=COLORS.get(label, "black"),
                label=LABELS.get(label, label))
    ax.set_xlabel(xlabel, fontsize=13)
    ax.set_ylabel("Events (unweighted)", fontsize=13)
    ax.set_title(title, fontsize=14)
    ax.legend(fontsize=10)
    ax.set_yscale("log")
    plt.tight_layout()
    plt.savefig(filename, dpi=150, transparent=True)
    print(f"  Saved: {filename}")
    plt.show()


print("\nPlotting...")

# 2-body invariant mass
plot_inv_mass(
    inv2,
    title=r"2-body invariant mass $M(\mu^+, e^-)$",
    xlabel=r"$M(\mu^+,\,e^-)$ [GeV]",
    bins=np.linspace(0, 500, 50),
    filename="inv_mass_2body.png",
)

# 4-body invariant mass
plot_inv_mass(
    inv4,
    title=r"4-body invariant mass $M(\mu^+, e^-, \bar{\nu}_e, \nu_\mu)$",
    xlabel=r"$M(\mu^+, e^-, \bar{\nu}_e, \nu_\mu)$ [GeV]",
    bins=np.linspace(0, 1000, 50),
    filename="inv_mass_4body.png",
)

# Overlay: 2-body vs 4-body for Background only
if "Background" in inv2 and len(inv2["Background"]) > 0:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].hist(inv2["Background"], bins=np.linspace(0, 500, 40),
                 histtype="stepfilled", alpha=0.7, color="#2166ac",
                 label="SM background")
    axes[0].set_xlabel(r"$M(\mu^+, e^-)$ [GeV]", fontsize=12)
    axes[0].set_ylabel("Events", fontsize=12)
    axes[0].set_title(r"2-body: $\mu^+$ and $e^-$", fontsize=13)
    axes[0].legend()

    if len(inv4.get("Background", [])) > 0:
        axes[1].hist(inv4["Background"], bins=np.linspace(0, 1000, 40),
                     histtype="stepfilled", alpha=0.7, color="#d6604d",
                     label="SM background")
        axes[1].set_xlabel(r"$M(\mu^+, e^-, \bar{\nu}_e, \nu_\mu)$ [GeV]",
                           fontsize=12)
        axes[1].set_ylabel("Events", fontsize=12)
        axes[1].set_title(r"4-body: all leptons", fontsize=13)
        axes[1].legend()

    plt.suptitle("Invariant mass distributions — SM Background", fontsize=14)
    plt.tight_layout()
    plt.savefig("inv_mass_background_comparison.png", dpi=150, transparent=True)
    print("  Saved: inv_mass_background_comparison.png")
    plt.show()

print("\nDone.")