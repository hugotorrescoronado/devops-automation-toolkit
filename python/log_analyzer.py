from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).parent.parent / "sample-logs" / "app.log"

counter = Counter()

with open(LOG_FILE, "r") as log:

    for line in log:

        if "ERROR" in line:
            counter["ERROR"] += 1

        if "WARNING" in line:
            counter["WARNING"] += 1

        if "INFO" in line:
            counter["INFO"] += 1

print("\n=== LOG ANALYSIS REPORT ===\n")

print(f"INFO Messages: {counter['INFO']}")
print(f"WARNING Messages: {counter['WARNING']}")
print(f"ERROR Messages: {counter['ERROR']}")