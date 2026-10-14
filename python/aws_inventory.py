import csv
import json
import os

REPORT_FILE = "reports/aws_inventory.csv"
SAMPLE_FILE = "sample-data/ec2_inventory.json"

inventory = []

try:
    import boto3

    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    print("Connected to AWS")

except Exception:

    print("AWS unavailable. Using sample inventory data.")

    with open(SAMPLE_FILE, "r") as file:

        response = json.load(file)

for reservation in response["Reservations"]:

    for instance in reservation["Instances"]:

        inventory.append(
            {
                "InstanceId": instance["InstanceId"],
                "InstanceType": instance["InstanceType"],
                "State": instance["State"]["Name"]
            }
        )

print("\n=== AWS INVENTORY REPORT ===\n")

for item in inventory:

    print(
        f"{item['InstanceId']} | "
        f"{item['InstanceType']} | "
        f"{item['State']}"
    )

os.makedirs("reports", exist_ok=True)

with open(REPORT_FILE, "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "InstanceId",
            "InstanceType",
            "State"
        ]
    )

    writer.writeheader()

    writer.writerows(inventory)

print(f"\nReport generated: {REPORT_FILE}")
