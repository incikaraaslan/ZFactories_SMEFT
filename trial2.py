import gzip
import numpy as np
import matplotlib.pyplot as plt

# =========================
# CONFIG
# =========================
L = 3000
sys = 0.02
bins = np.linspace(0, 500, 20)

# PDG IDs
ELECTRON = 11


# =========================
# SMART FILE READER
# =========================
def open_any(file):
    if file.endswith(".gz"):
        return gzip.open(file, "rt")
    else:
        return open(file, "r")


# =========================
# LHE PARSER (ROBUST MG5 STYLE)
# =========================
def load_lhe(file):
    events = []

    with open_any(file) as f:
        lines = f.readlines()

    i = 0
    nlines = len(lines)

    while i < nlines:

        # find event start
        if "<event>" not in lines[i]:
            i += 1
            continue

        i += 1

        # event header
        header = lines[i].split()
        if len(header) == 0:
            continue

        try:
            n_particles = int(header[0])
        except:
            i += 1
            continue

        i += 1

        event = []

        for _ in range(n_particles):
            if i >= nlines:
                break

            parts = lines[i].split()
            i += 1

            if len(parts) < 10:
                continue

            try:
                pid = int(parts[0])
                status = int(parts[1])

                px = float(parts[6])
                py = float(parts[7])
                pz = float(parts[8])
                E  = float(parts[9])

                event.append((pid, status, px, py, pz, E))

            except:
                continue

        events.append(event)

    return events


# =========================
# PHYSICS OBJECTS
# =========================
def pt(px, py):
    return np.sqrt(px**2 + py**2)


def get_leptons(events, pid_target):
    pts = []

    for ev in events:
        for pid, status, px, py, pz, E in ev:

            # final-state only (IMPORTANT FIX)
            if status != 1:
                continue

            if abs(pid) == pid_target:
                pts.append(pt(px, py))

    return np.array(pts)


# =========================
# LOAD FILES
# =========================
sm_file  ="./LHEfiles/SMbckg_ZWvee.lhe" # "./LHEfiles/SM_ZW.lhe"
eft_file = "./LHEfiles/QeW_ppvmmveequad.lhe" # "./LHEfiles/SMEFT_OeW.lhe"

sm_events  = load_lhe(sm_file)
eft_events = load_lhe(eft_file)


print("SM events loaded:", len(sm_events))
print("EFT events loaded:", len(eft_events))


# =========================
# OBSERVABLE
# =========================
pt_sm  = get_leptons(sm_events, ELECTRON)
pt_eft = get_leptons(eft_events, ELECTRON)


print("SM leptons:", len(pt_sm))
print("EFT leptons:", len(pt_eft))


# =========================
# HISTOGRAMS
# =========================
h_sm, _  = np.histogram(pt_sm, bins=bins)
h_eft, _ = np.histogram(pt_eft, bins=bins)

template = h_eft - h_sm


# =========================
# SANITY CHECKS (VERY IMPORTANT)
# =========================
print("\n=== SANITY CHECK ===")
print("Total SM entries:", np.sum(h_sm))
print("Total EFT entries:", np.sum(h_eft))
print("Max bin diff:", np.max(np.abs(template)))


# =========================
# PURE MC STATISTICS (NO LUMINOSITY YET)
# =========================
sigma_stat = np.sqrt(np.maximum(h_sm, 1))
sigma_sys  = sys * h_sm

sigma_tot = np.sqrt(sigma_stat**2 + sigma_sys**2)
sigma_tot = np.where(sigma_tot < 1e-8, 1e-8, sigma_tot)


# =========================
# χ² MODEL (CLEAN EFT FORM)
# =========================
def chi2(Lambda):

    scale = 1.0 / Lambda**2
    dN = template * scale

    chi = np.sum((dN / sigma_tot)**2)

    return chi


# =========================
# SCAN
# =========================
Lvals = np.linspace(0.5, 15, 200)
chi_vals = np.array([chi2(Lv) for Lv in Lvals])


# =========================
# LIMIT
# =========================
idx = np.where(chi_vals < 3.84)[0]

Lambda_limit = Lvals[idx[0]] if len(idx) > 0 else None

print("\n========================")
print("95% CL Λ LIMIT:", Lambda_limit, "TeV")
print("========================")


# =========================
# PLOT
# =========================
plt.plot(Lvals, chi_vals)
plt.axhline(3.84, color='red', linestyle='--')
plt.xlabel("Λ [TeV]")
plt.ylabel("χ²")
plt.title("Clean LHE SMEFT fit")
plt.show()