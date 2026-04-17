import subprocess
import re
import os

# === USER SETTINGS ===
MG5_PATH = "../../MG5_aMC_v3_6_3/bin/mg5_aMC"
PROCESS = "mu+ mu- > mu- z vm~ w+"
EBEAM = 5000.0   # 10 TeV collider (5 TeV per beam)
NEVENTS = 100
OUTDIR = "eta_scan_results_mumu_muzwnu"
ETA_MAX_LIST = [2.5, 3.0, 4.0, 5.0, 6.0]  # η cuts to test

os.makedirs(OUTDIR, exist_ok=True)

def make_mg_input(eta_min):
    return f"""
    import model sm-lepton_masses
    set group_subprocesses False
    generate {PROCESS}
    output {OUTDIR}/proc_eta{eta_min}
    launch
    set nevents {NEVENTS}
    set ebeam1 5000.0 # for 10 TeV collisions
    set ebeam2 5000.0 
    set lpp1 0
    set lpp2 0
    """ + """
    set eta_min_pdg {13:"""+ f"""{eta_min}"""+ """}
    quit
    """

def run_mg5(mg_input, label):
    input_file = f"{OUTDIR}/run_{label}.txt"
    with open(input_file, "w") as f:
        f.write(mg_input)
    result = subprocess.run(
        [MG5_PATH, input_file],
        capture_output=True,
        text=True
    )
    # Try to extract cross section from output
    match = re.search(r"Cross-section\s*:\s*([\d.Ee+-]+)", result.stdout)
    if match:
        xsec = float(match.group(1))
    else:
        xsec = None
    return xsec, result.stdout

# === MAIN SCAN LOOP ===
results = {}
for eta in ETA_MAX_LIST:
    print(f"\n>>> Running MG5 for etal = {eta}")
    mg_input = make_mg_input(eta)
    xsec, log = run_mg5(mg_input, f"eta{eta}")
    results[eta] = xsec
    if xsec:
        print(f"Cross section for eta_min={eta}: {xsec} pb")
    else:
        print(f"Could not find cross section in output for eta_min={eta}")

# === SAVE SUMMARY ===
summary_file = f"{OUTDIR}/xsec_summary.txt"
with open(summary_file, "w") as f:
    for eta, xsec in results.items():
        f.write(f"eta_max={eta}\t{xsec if xsec else 'N/A'}\n")

print("\nScan complete! Summary saved to", summary_file)
