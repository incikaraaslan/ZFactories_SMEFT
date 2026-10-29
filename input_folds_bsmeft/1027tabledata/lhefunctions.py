import numpy as np
import gzip
import matplotlib.pyplot as plt
import os
import re
try:
    import pandas as pd
except Exception:
    pd = None

try:
    from mt2 import mt2 as mt2_fn
except Exception:
    mt2_fn = None

def _open_lhe(path):
    return gzip.open(path, "rt") if str(path).endswith(".gz") else open(path, "rt")


def _to_table(rows, as_dataframe="auto"):
    if as_dataframe == "auto":
        as_dataframe = (pd is not None)

    if as_dataframe:
        if pd is None:
            raise ImportError(
                "pandas is not installed. Use as_dataframe=False or remove DataFrame output."
            )
        return pd.DataFrame(rows)

    return rows


def read_lhe_events(lhe_path, statuses=(1,)):
    """
    Read an LHE/LHE.GZ file into a list of events.

    Parameters
    ----------
    lhe_path : str
        Path to .lhe or .lhe.gz file.
    statuses : iterable of int or None
        Particle status codes to keep.
        Use (1,) for final-state outgoing particles.
        Use None to keep all particle records in each event.
    """
    events = []
    in_event = False
    skip_event_info = False
    current_event = []

    status_set = None if statuses is None else set(statuses)

    with _open_lhe(lhe_path) as f:
        for line in f:
            s = line.strip()

            if s == "<event>":
                in_event = True
                skip_event_info = True
                current_event = []
                continue

            if s == "</event>":
                events.append(current_event)
                in_event = False
                continue

            if not in_event or not s or s.startswith("#") or s.startswith("<"):
                continue

            if skip_event_info:
                skip_event_info = False
                continue

            cols = s.split()
            if len(cols) < 13:
                continue

            p = {
                "pid": int(cols[0]),
                "status": int(cols[1]),
                "mother1": int(cols[2]),
                "mother2": int(cols[3]),
                "color1": int(cols[4]),
                "color2": int(cols[5]),
                "px": float(cols[6]),
                "py": float(cols[7]),
                "pz": float(cols[8]),
                "E": float(cols[9]),
                "m": float(cols[10]),
                "vtim": float(cols[11]),
                "spin": float(cols[12]),
            }

            if status_set is None or p["status"] in status_set:
                current_event.append(p)

    return events


def read_lhe_outgoing(lhe_path):
    return read_lhe_events(lhe_path, statuses=(1,))


def pt(p):
    return np.hypot(p["px"], p["py"])


def p3(p):
    return np.sqrt(p["px"]**2 + p["py"]**2 + p["pz"]**2)


def phi(p):
    return np.arctan2(p["py"], p["px"])


def theta(p):
    denom = max(p3(p), 1e-15)
    return np.arccos(np.clip(p["pz"] / denom, -1.0, 1.0))


def eta(p):
    pabs = p3(p)
    if np.isclose(pabs, abs(p["pz"])):
        return np.sign(p["pz"]) * np.inf
    return 0.5 * np.log((pabs + p["pz"]) / (pabs - p["pz"]))


def fourvec(p):
    return np.array([p["E"], p["px"], p["py"], p["pz"]], dtype=float)


def inv_mass(*particles):
    q = np.sum([fourvec(p) for p in particles], axis=0)
    m2 = q[0]**2 - q[1]**2 - q[2]**2 - q[3]**2
    return np.sqrt(max(m2, 0.0))


def delta_phi(p1, p2):
    dphi = phi(p1) - phi(p2)
    return np.arctan2(np.sin(dphi), np.cos(dphi))


def delta_r(p1, p2):
    return np.hypot(eta(p1) - eta(p2), delta_phi(p1, p2))


def pair_pt(p1, p2):
    return np.hypot(p1["px"] + p2["px"], p1["py"] + p2["py"])


def met_from_particles(particles):
    if len(particles) == 0:
        return 0.0, 0.0, 0.0, 0.0
    px = sum(p["px"] for p in particles)
    py = sum(p["py"] for p in particles)
    met = np.hypot(px, py)
    met_phi = np.arctan2(py, px)
    return met, met_phi, px, py


def pid_is(*pids):
    wanted = set(pids)
    return lambda p: p["pid"] in wanted


def abs_pid_is(*abs_pids):
    wanted = set(abs_pids)
    return lambda p: abs(p["pid"]) in wanted


def combine_or(*selectors):
    return lambda p: any(sel(p) for sel in selectors)


def combine_and(*selectors):
    return lambda p: all(sel(p) for sel in selectors)


def _sort_particles(particles, sort_by="pt"):
    parts = list(particles)

    if sort_by == "pt":
        parts.sort(key=pt, reverse=True)
    elif sort_by == "E":
        parts.sort(key=lambda p: p["E"], reverse=True)
    elif sort_by is None:
        pass
    else:
        raise ValueError("sort_by must be 'pt', 'E', or None")

    return parts


def event_table(event, sort_by="pt", as_dataframe="auto"):
    parts = _sort_particles(event, sort_by=sort_by)

    rows = []
    for i, p in enumerate(parts):
        rows.append({
            "idx": i,
            "pid": p["pid"],
            "status": p["status"],
            "pt": pt(p),
            "eta": eta(p),
            "phi": phi(p),
            "theta": theta(p),
            "E": p["E"],
            "m": p["m"],
            "px": p["px"],
            "py": p["py"],
            "pz": p["pz"],
        })

    return _to_table(rows, as_dataframe=as_dataframe)


def analyze_pair_events(
    lhe_path,
    sel1,
    sel2,
    which1=0,
    which2=0,
    invisible=None,
    sort_by="pt",
    mt2_test_mass=0.0,
    as_dataframe="auto",
):
    events = read_lhe_outgoing(lhe_path)
    rows = []

    for ievt, event in enumerate(events):
        parts1 = _sort_particles([p for p in event if sel1(p)], sort_by=sort_by)
        parts2 = _sort_particles([p for p in event if sel2(p)], sort_by=sort_by)

        if len(parts1) <= which1 or len(parts2) <= which2:
            continue

        p1 = parts1[which1]
        p2 = parts2[which2]

        if p1 is p2:
            continue

        invisible_parts = [p for p in event if invisible(p)] if invisible else []
        met, met_phi, met_px, met_py = met_from_particles(invisible_parts)

        row = {
            "event": ievt,
            "pid1": p1["pid"],
            "pid2": p2["pid"],
            "pt1": pt(p1),
            "pt2": pt(p2),
            "eta1": eta(p1),
            "eta2": eta(p2),
            "phi1": phi(p1),
            "phi2": phi(p2),
            "E1": p1["E"],
            "E2": p2["E"],
            "m1": p1["m"],
            "m2": p2["m"],
            "deltaPhi": delta_phi(p1, p2),
            "deltaEta": eta(p1) - eta(p2),
            "deltaR": delta_r(p1, p2),
            "m12": inv_mass(p1, p2),
            "pt12": pair_pt(p1, p2),
            "MET": met,
            "MET_phi": met_phi,
            "MET_px": met_px,
            "MET_py": met_py,
            "n_invisible": len(invisible_parts),
        }

        if mt2_fn is not None and invisible is not None and len(invisible_parts) > 0:
            row["MT2"] = mt2_fn(
                p1["m"], p1["px"], p1["py"],
                p2["m"], p2["px"], p2["py"],
                met_px, met_py,
                mt2_test_mass, mt2_test_mass,
            )
        else:
            row["MT2"] = np.nan

        rows.append(row)

    return _to_table(rows, as_dataframe=as_dataframe)

# READ CROSS-SECTIONS 
def extract_cross_section(filepath):
    """
    Parses a text file to find the first non-comment, non-empty line
    and extracts the numerical cross-section in pb.
    """
    if not os.path.exists(filepath):
        print(f"Warning: File not found {filepath}. Setting dummy cross section = 1.0 pb.")
        return 1.0

    with open(filepath, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                match = re.search(r"[-+]?\d+\.\d+([eE][-+]?\d+)?", stripped)
                if match:
                    return float(match.group(0))
    raise ValueError(f"No valid numerical cross-section found in {filepath}")