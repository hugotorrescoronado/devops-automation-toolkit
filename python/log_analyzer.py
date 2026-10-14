from collections import Counter

counter = Counter()

with open("sample-logs/app.log", "r") as log:

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