import os
import subprocess
import re
import json

# ==============================================================================
# CONFIGURATION
# ==============================================================================
MG5_PATH = "/home/incik/MG5_aMC_v3_6_3/bin/mg5_aMC"  # Update to your actual MadGraph path
MODEL_NAME = "/home/incik/MG5_aMC_v3_6_3/models/VectorSinglet_d6_UFO_HC_extended"      # Your updated FeynRules UFO model
OUTPUT_DIR = "mg5_z_decay_scan"

# Physics Parameters
LAMBDA_0 = 1000.0  # Benchmark scale used in MG5 (GeV)
GAMMA_Z_SM = 2.4952  # Total Z width in SM (GeV)

# Maximum allowed width for new physics (e.g., experimental uncertainty ~ 1.5 MeV)
GAMMA_ALLOWED = 0.0015  

# Mass scan range: 1 GeV to 40 GeV in steps of 5
mass_points = list(range(1, 41, 5)) 

results = {}

# ==============================================================================
# AUTOMATION LOOP
# ==============================================================================
for mx in mass_points:
    print(f"\n[+] Running MadGraph baseline for M_X = {mx} GeV...")
    
    # Define unique run name
    run_name = f"run_mx_{mx}"
    cmd_filename = f"mg5_cmd_mx_{mx}.txt"
    
    # Construct the MadGraph command script
    mg5_commands = f"""
    import model {MODEL_NAME}
    define f = e- mu- ta- e+ mu+ ta- ve vm vt ve~ vm~ vt~
    generate z > u u~ f f f f VBEFT=1
    add process z > d d~ f f f f VBEFT=1
    add process z > s s~ f f f f VBEFT=1
    add process z > c c~ f f f f VBEFT=1
    output {OUTPUT_DIR}_{run_name}
    launch
    set MX {mx}
    set nevents 10000
    set ebeam1 6500
    set ebeam2 6500
    set pdlabel lhapdf
    set lhaid 315000
    set LamX 1000
    set lpp1 0
    set lpp2 0
    set LamX {LAMBDA_0}
    """
    
    with open(cmd_filename, "w") as f:
        f.write(mg5_commands)
        
    # Execute MadGraph
    try:
        subprocess.run([MG5_PATH, cmd_filename], check=True)
    except FileNotFoundError:
        print(f"[!] Error: Could not find MadGraph at '{MG5_PATH}'. Please update the path.")
        break

    # Clean up command file
    if os.path.exists(cmd_filename):
        os.remove(cmd_filename)
        
    # Parse the resulting width from the SubProcesses/results.dat file
    # For a 1-particle initial state decay, the 'cross section' column is the width in GeV
    results_path = os.path.join(f"{OUTPUT_DIR}_{run_name}", "SubProcesses", "results.dat")
    
    if os.path.exists(results_path):
        with open(results_path, "r") as f:
            lines = f.readlines()
            if lines:
                # Typically the last line or the line containing the cross section/width
                match = re.search(r"^\s*([\d\.eE\-\+]+)", lines[-1])
                if match:
                    gamma_0 = float(match.group(1))
                    
                    # Calculate Lambda_min using the scaling relation:
                    # Lambda_min = Lambda_0 * (Gamma_0 / Gamma_allowed)**(1/4)
                    if gamma_0 > 0:
                        lambda_min = LAMBDA_0 * ((gamma_0 / GAMMA_ALLOWED) ** 0.25)
                    else:
                        lambda_min = 0.0
                        
                    print(f"    -> Extracted Gamma_0 = {gamma_0:.6e} GeV")
                    print(f"    -> Calculated Lambda_min = {lambda_min:.2f} GeV")
                    
                    results[mx] = {
                        "gamma_0": gamma_0,
                        "lambda_min": lambda_min
                    }
    else:
        print(f"[!] Warning: Could not find results file at {results_path}")

# Save data out to a JSON file for the plotting script
with open("scan_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("\n[+] Scan complete. Data saved to 'scan_results.json'.")