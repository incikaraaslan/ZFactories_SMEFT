import numpy as np
import matplotlib.pyplot as plt
import gzip
# -------------------------------
# SETTINGS
# -------------------------------
L = 3000  # HL-LHC luminosity in fb^-1


import gzip
import re

def extract_xsec_lhe_gz(file):
    with gzip.open(file, "rt") as f:
        lines = f.readlines()

    # ----------------------------
    # METHOD 1: look in <init> block
    # ----------------------------
    in_init = False
    init_lines = []

    for line in lines:
        if "<init>" in line:
            in_init = True
            continue
        if "</init>" in line:
            break
        if in_init:
            init_lines.append(line.strip())

    # MG5 usually puts xsec in first numeric block of init
    for line in init_lines:
        nums = re.findall(r"[-+]?\d*\.\d+e?[+-]?\d*", line)
        if len(nums) >= 1:
            try:
                val = float(nums[0])
                if val > 0:
                    return val
            except:
                continue

    # ----------------------------
    # METHOD 2: fallback scan entire file
    # ----------------------------
    for line in lines:
        if "cross" in line.lower():
            nums = re.findall(r"[-+]?\d*\.\d+e?[+-]?\d*", line)
            if nums:
                return float(nums[0])

    raise ValueError("Cross section not found in LHE file (MG5 format mismatch)")
# SIMPLE LHE READER (cross section extraction)
# -------------------------------
def extract_xsec(lhe_file):
    with open(lhe_file, "r") as f:
        for line in f:
            if "<init>" in line:
                break

        for line in f:
            if line.strip().startswith("#") or line.strip() == "":
                continue
            if "<event>" in line:
                break

        # MG5 stores xsec in header:
    with open(lhe_file, "r") as f:
        for line in f:
            if "Integrated weight" in line or "Integrated cross section" in line:
                try:
                    return float(line.split()[4])
                except:
                    pass

    raise ValueError("Cross section not found in LHE file")

def extract_xsec_from_txt(txt_file):
    with open(txt_file, "r") as f:
        for line in f:
            line = line.strip()

            # skip comments
            if line.startswith("#") or line == "":
                continue

            parts = line.split()

            # look for run_XX lines
            if parts[0].startswith("run_"):
                try:
                    xsec = float(parts[2])   # cross section column
                    err  = float(parts[3])   # error column
                    nev  = float(parts[4])   # events

                    return xsec, err, nev
                except Exception as e:
                    continue

    raise ValueError("No valid MG5 run line found in txt file")
# -------------------------------
# LOAD CROSS SECTIONS
# -------------------------------
sigma_SM, err_SM, N_SM = extract_xsec_from_txt("/home/incik/ZFactories_SMEFT/output_folds/SM_ZW.txt")
sigma_EFT, err_EFT, N_EFT = extract_xsec_from_txt("/home/incik/ZFactories_SMEFT/output_folds/SMEFT_OeW.txt")

print("SM cross section:", sigma_SM, "pb")
print("SMEFT cross section:", sigma_EFT, "pb")


# -------------------------------
# EFT DEVIATION
# -------------------------------
delta_sigma = sigma_EFT - sigma_SM

print("Delta sigma:", delta_sigma, "pb")

# -------------------------------
# EFT SCALING DIAGNOSTIC
# -------------------------------

for L in [1, 2, 3, 5, 10]:
    lin = delta_sigma / (1 / L**2)
    quad = delta_sigma / (1 / L**4)

    print(f"Lambda={L} TeV  linear-scaling test={lin:.6f}  quadratic-scaling test={quad:.6f}")
    
# -------------------------------
# EVENT COUNTS AT HL-LHC
# -------------------------------
N_SM = sigma_SM * L
delta_N = delta_sigma * L

print("SM events:", N_SM)
print("EFT shift:", delta_N)

# -------------------------------
# SIMPLE STATISTICAL TEST
# -------------------------------
epsilon_sys = 0.02  # 2% systematics

sigma_tot_error = np.sqrt(N_SM + (epsilon_sys * N_SM)**2)

chi = delta_N / sigma_tot_error

print("Significance (sigma):", chi)

# -------------------------------
# SCAN OVER LAMBDA
# (assume scaling ~ 1/Lambda^2 or 1/Lambda^4)
# -------------------------------

Lambda_vals = np.linspace(0.5, 15, 200)  # TeV
chi_vals = []

# rescale EFT effect (assume linear scaling first)
for Lam in Lambda_vals:
    scale = (1.0 / Lam**2)  # since you used 1 TeV normalization
    delta_N_L = delta_N * scale
    chi_L = delta_N_L / sigma_tot_error
    chi_vals.append(chi_L)

chi_vals = np.array(chi_vals)

# -------------------------------
# FIND 95% CL LIMIT
# -------------------------------
idx = np.where(np.abs(chi_vals) < 1.96)[0]

if len(idx) > 0:
    Lambda_limit = Lambda_vals[idx[0]]
else:
    Lambda_limit = None

print("\n===== RESULT =====")
print("95% CL Lambda limit ~", Lambda_limit, "TeV")

# -------------------------------
# PLOT
# -------------------------------
plt.plot(Lambda_vals, chi_vals)
plt.axhline(1.96, color='red', linestyle='--')
plt.xlabel("Lambda [TeV]")
plt.ylabel("Significance (sigma)")
plt.title("HL-LHC sensitivity to O_eW")
plt.show()