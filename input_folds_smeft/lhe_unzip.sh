#!/bin/bash
set -e

if [ $# -lt 2 ]; then
  echo "Usage: $0 MG_OUTPUT_DIR DEST_DIR"
  echo "Example:"
  echo "  $0 ../output_folds/SMbckg_ZWvee ../LHEfiles"
  exit 1
fi

OUT="$1"
DEST="$2"

EVENTS="$OUT/Events"

if [ ! -d "$EVENTS" ]; then
  echo "Error: $EVENTS does not exist"
  exit 1
fi

# Find the latest run directory (run_01, run_02, ...)
RUN=$(ls -d "$EVENTS"/run_* 2>/dev/null | sort | tail -n 1)

if [ -z "$RUN" ]; then
  echo "Error: no run_* directory found in $EVENTS"
  exit 1
fi

LHE_GZ="$RUN/unweighted_events.lhe.gz"
LHE="$RUN/unweighted_events.lhe"

if [ -f "$LHE_GZ" ]; then
  SRC="$LHE_GZ"
elif [ -f "$LHE" ]; then
  SRC="$LHE"
else
  echo "Error: no LHE file found in $RUN"
  exit 1
fi

mkdir -p "$DEST"

cp "$SRC" "$DEST/"

# Unzip if needed
if [[ "$SRC" == *.gz ]]; then
  gunzip -f "$DEST/$(basename "$SRC")"
  FINAL="$DEST/$(basename "$SRC" .gz)"
else
  FINAL="$DEST/$(basename "$SRC")"
fi

# Rename LHE to the MG output folder name
FINAL="$DEST/$(basename "$OUT").lhe"
mv "$DEST/unweighted_events.lhe" "$FINAL"

echo "LHE copied to:"
echo "  $FINAL"
