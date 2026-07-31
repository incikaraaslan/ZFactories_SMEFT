import gzip
import numpy as np
import matplotlib.pyplot as plt
 
# =========================
# CONFIG
# =========================
L          = 3000       # HL-LHC luminosity [fb^-1]
sys_unc    = 0.02       # 2% flat systematic on SM background
LAMBDA_GEN = 1.0        # TeV — reference scale used in MadGraph generation
bins       = np.linspace(0, 500, 20)
ELECTRON   = 11
 
# =========================
# FILE UTILITIES
# =========================
def open_any(path):
    return gzip.open(path, "rt") if path.endswith(".gz") else open(path, "r")
 
 
def parse_xsec(path):
    """
    Read total cross section [pb] from the LHE <init> block.
 
    Standard LHE structure inside <init>:
      Line 1 : beam info (2 PDGs, energies, PDF info, ...)
      Line 2+: one line per process  →  xsec [pb]  xerr  xmax  process_id
 
    Returns the sum over all processes (handles multi-process LHE files).
    """
    xsec_total = 0.0
    with open_any(path) as f:
        in_init   = False
        beam_done = False
        for line in f:
            s = line.strip()
            if "<init>" in s:
                in_init   = True
                beam_done = False
                continue
            if "</init>" in s:
                break
            if not in_init or not s or s.startswith("#"):
                continue
            if not beam_done:          # skip first line (beam kinematics)
                beam_done = True
                continue
            parts = s.split()
            try:
                xsec_total += float(parts[0])
            except (ValueError, IndexError):
                pass
    return xsec_total
 
 
def load_lhe(path):
    """Return list of events; each event is a list of (pid, status, px, py)."""
    events = []
    with open_any(path) as f:
        lines = f.readlines()
 
    i = 0
    while i < len(lines):
        if "<event>" not in lines[i]:
            i += 1
            continue
        i += 1                              # skip <event> tag
        header = lines[i].split()
        i += 1
        try:
            n_particles = int(header[0])
        except (ValueError, IndexError):
            continue
 
        event = []
        for _ in range(n_particles):
            if i >= len(lines):
                break
            parts = lines[i].split()
            i += 1
            if len(parts) < 10:
                continue
            try:
                event.append((
                    int(parts[0]),    # pid
                    int(parts[1]),    # status
                    float(parts[6]),  # px
                    float(parts[7]),  # py
                ))
            except (ValueError, IndexError):
                continue
        events.append(event)
    return events
 
 
# =========================
# OBSERVABLE
# =========================
def get_electron_pt(events):
    pts = []
    for ev in events:
        for pid, status, px, py in ev:
            if status == 1 and abs(pid) == ELECTRON:
                pts.append(np.hypot(px, py))
    return np.array(pts)
 
 
# =========================
# LOAD FILES
# =========================
sm_file  = "./LHEfiles/SMbckg_ZWvee.lhe"
eft_file = "./LHEfiles/QeW_ppvmmveequad.lhe"
 
print("── Parsing cross sections from LHE headers ──")
xsec_sm   = parse_xsec(sm_file)    # pb
xsec_quad = parse_xsec(eft_file)   # pb  (at Lambda_gen = 1 TeV, c_eW = 1)
 
print(f"  σ_SM        = {xsec_sm:.4e} pb")
print(f"  σ_quad      = {xsec_quad:.4e} pb   [Λ = {LAMBDA_GEN} TeV, c_eW = 1]")
 
sm_events  = load_lhe(sm_file)
eft_events = load_lhe(eft_file)
 
N_mc_sm   = len(sm_events)
N_mc_quad = len(eft_events)
 
print(f"\n  N_MC SM     = {N_mc_sm}")
print(f"  N_MC quad   = {N_mc_quad}")
 
pt_sm  = get_electron_pt(sm_events)
pt_eft = get_electron_pt(eft_events)
 
# =========================
# LUMINOSITY WEIGHTS
# =========================
# Each MC event represents  (sigma * L / N_MC)  physical events.
# This is the ONLY correct way to compare samples with different
# generation cross sections and event counts.
 
w_sm   = xsec_sm   * L / N_mc_sm     # physical events per MC event
w_quad = xsec_quad * L / N_mc_quad
 
print(f"\n  w_SM        = {w_sm:.4f}  events / MC event")
print(f"  w_quad      = {w_quad:.4f}  events / MC event")
 
# =========================
# WEIGHTED HISTOGRAMS
# =========================
h_sm,   _ = np.histogram(pt_sm,  bins=bins, weights=np.full(len(pt_sm),  w_sm))
h_quad, _ = np.histogram(pt_eft, bins=bins, weights=np.full(len(pt_eft), w_quad))
 
# ─────────────────────────────────────────────────────────────────
# KEY FIX 1: DO NOT subtract h_sm from h_quad.
#
# The quad LHE file is the PURE |EFT|² contribution — it contains
# NO SM events. Subtracting h_sm would remove physics that was
# never in the file and produce negative bins.
#
# Correct signal template = h_quad directly.
# ─────────────────────────────────────────────────────────────────
T_quad = h_quad   # events at Lambda = LAMBDA_GEN TeV, c_eW = 1
 
# =========================
# UNCERTAINTY ON SM BACKGROUND
# =========================
sigma_stat = np.sqrt(np.maximum(h_sm, 1.0))   # Poisson floor
sigma_sys  = sys_unc * h_sm                    # flat 2% systematic
sigma_tot  = np.sqrt(sigma_stat**2 + sigma_sys**2)
sigma_tot  = np.where(sigma_tot < 1e-8, 1e-8, sigma_tot)   # avoid /0
 
# =========================
# χ² FUNCTION
# =========================
# Total prediction:  N(Λ) = N_SM  +  T_quad / Λ⁴
#
# The 1/Λ⁴ scaling is exact for the pure quadratic EFT term because:
#
#   d σ_quad / d pT  ∝  |M_EFT|²  ∝  (c_eW / Λ²)²  =  c²_eW / Λ⁴
#
# The template T_quad was generated at Λ = LAMBDA_GEN = 1 TeV, so
# to rescale to an arbitrary Λ:
#
#   ΔN(Λ) = T_quad × (LAMBDA_GEN / Λ)⁴  =  T_quad / Λ⁴   (LAMBDA_GEN = 1)
#
# ─────────────────────────────────────────────────────────────────
# KEY FIX 2: USE Λ⁴ NOT Λ² in the denominator.
#
# The old code used  scale = 1/Λ²,  then squared inside chi2,
# giving effectively  1/Λ⁴.  But the template itself also scales
# as 1/Λ⁴, so the combined exponent became 1/Λ⁸ — while the code
# *solved* for the 1/Λ⁴ crossing, inflating Λ_lim by
#   (S/3.84)^(1/4)  instead of the correct  (S/3.84)^(1/8).
# ─────────────────────────────────────────────────────────────────
 
def chi2(Lambda):
    dN = T_quad * (LAMBDA_GEN / Lambda)**4    # correct quad rescaling
    return np.sum((dN / sigma_tot)**2)
 
# =========================
# ANALYTIC LIMIT
# =========================
# chi2(Λ) = S / Λ⁸   where  S = Σ_i [ T_quad^i / σ_tot^i ]²
# 95% CL:  chi2 = 3.84  →  Λ_lim = (S / 3.84)^(1/8)
 
S = np.sum((T_quad / sigma_tot)**2)
Lambda_analytic = (S / 3.84) ** (1.0 / 8.0)
 
print(f"\n  Sensitivity integral  S  = {S:.4e}")
print(f"  Analytic limit  (S/3.84)^(1/8)  = {Lambda_analytic:.2f} TeV")
 
# =========================
# NUMERICAL SCAN
# =========================
Lambda_vals = np.linspace(0.5, 15, 500)
chi_vals    = np.array([chi2(Lv) for Lv in Lambda_vals])
 
crossing     = np.where(chi_vals < 3.84)[0]
Lambda_limit = Lambda_vals[crossing[0]] if len(crossing) > 0 else None
 
print(f"\n{'='*45}")
if Lambda_limit:
    print(f"  95% CL LIMIT ON Λ (O_eW) :  {Lambda_limit:.2f} TeV")
else:
    print("  No crossing found — increase scan range or check normalisation")
print(f"{'='*45}\n")
 
# =========================
# SANITY CHECKS
# =========================
print("── Sanity checks ──")
print(f"  Total SM events @ {L} fb⁻¹    : {np.sum(h_sm):.1f}")
print(f"  Total quad events @ {L} fb⁻¹  : {np.sum(T_quad):.1f}  [Λ = {LAMBDA_GEN} TeV]")
print(f"  Negative template bins        : {np.sum(T_quad < 0)}")
print(f"  chi2 at Λ = 1 TeV             : {chi2(1.0):.2e}")
print(f"  chi2 at Λ = 5 TeV             : {chi2(5.0):.2e}")
 
# =========================
# PLOTS
# =========================
bin_centers = 0.5 * (bins[:-1] + bins[1:])
bin_widths  = np.diff(bins)
 
# ── Plot 1: Weighted pT distributions ──────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(bin_centers, h_sm,   width=bin_widths, alpha=0.6,
       color='steelblue', label='SM background')
ax.bar(bin_centers, T_quad, width=bin_widths, alpha=0.6,
       color='firebrick',
       label=rf'$\mathcal{{O}}_{{eW}}$ quad  ($\Lambda={LAMBDA_GEN}$ TeV, $c_{{eW}}=1$)')
ax.set_xlabel(r'Electron $p_T$ [GeV]', fontsize=13)
ax.set_ylabel(fr'Events / bin   ($\mathcal{{L}}={L}$ fb$^{{-1}}$)', fontsize=12)
ax.set_title(r'$p_T^e$ distribution: SM vs pure EFT² contribution', fontsize=13)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('pt_distributions.png', dpi=150)
plt.show()
 
# ── Plot 2: χ² vs Λ ────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(Lambda_vals, chi_vals, color='navy', lw=2,
        label=r'$\chi^2(\Lambda) = \mathcal{S}\,/\,\Lambda^8$')
ax.axhline(3.84, color='red', ls='--', lw=1.5,
           label=r'95% CL  ($\chi^2 = 3.84$)')
if Lambda_limit:
    ax.axvline(Lambda_limit, color='green', ls=':', lw=1.8,
               label=fr'$\Lambda_{{\rm lim}} = {Lambda_limit:.1f}$ TeV')
ax.set_xlabel(r'$\Lambda$ [TeV]', fontsize=13)
ax.set_ylabel(r'$\chi^2$', fontsize=13)
ax.set_title(
    fr'Physics reach: $\mathcal{{O}}_{{eW}}$  (HL-LHC, $\mathcal{{L}}={L}$ fb$^{{-1}}$)',
    fontsize=13)
ax.set_xlim(Lambda_vals[0], 1.5)#Lambda_vals[-1])
ax.set_ylim(0, min(chi_vals.max() * 1.1, 300))
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('chi2_vs_lambda.png', dpi=150)
plt.show()
 
# ── Plot 3: Signal / background ratio ──────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
ratio = T_quad / np.maximum(h_sm, 1e-8)
ax.bar(bin_centers, ratio, width=bin_widths, color='darkorange', alpha=0.85)
ax.set_xlabel(r'Electron $p_T$ [GeV]', fontsize=13)
ax.set_ylabel(
    rf'$T^i_{{\rm quad}}\,/\,h^i_{{\rm SM}}$   ($\Lambda={LAMBDA_GEN}$ TeV)',
    fontsize=12)
ax.set_title(r'EFT signal / SM background ratio per $p_T$ bin', fontsize=13)
plt.tight_layout()
plt.savefig('s_over_b.png', dpi=150)
plt.show()