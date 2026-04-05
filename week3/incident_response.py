#!/usr/bin/env python3
import subprocess
import json

print("[*] Initiating Automated Threat Hunt...")

import subprocess
import json

# PHASE 1: Use grep to find failed login attempts
result = subprocess.run(
    ["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"],
    capture_output=True,
    text=True
)

raw_output = result.stdout

# PHASE 2: Data Parsing
# Split the large block of text into a list of strings (lines)
lines = raw_output.strip().split('\n')

attacker_ips = []

for line in lines:
    if line:
        # In these logs, the IP address is usually at index 10
        # Example: "... from 192.168.1.5 port ..."
        parts = line.split(" ")
        if len(parts) > 10:
            ip = parts[10]
            attacker_ips.append(ip)

# Ensure we only have unique IPs to keep the report clean
unique_attackers = list(set(attacker_ips))

# Create the alert structure
alert_data = {
    "alert_type": "Brute Force",
    "attacker_ips": unique_attackers,
    "count": len(unique_attackers)
}

# Write to the JSON file
with open("threat_report.json", "w") as file:
    json.dump(alert_data, file, indent=4)

print("[+] Incident Response Complete. Report generated: threat_report.json")

# TASK 1: Use subprocess to grep for "Failed password" in /var/log/titan_sim/auth_sim.log
# Ensure you capture the output and convert it to text!
# YOUR CODE HERE:


# TASK 2: Parse the captured output to extract ONLY the attacking IP addresses.
# Hint: Loop through each line, split the line by spaces, and grab index [10].
# Save the IPs to a Python List called attacker_ips.
# YOUR CODE HERE:


# TASK 3: Create a dictionary containing the extracted IPs and export it to 'threat_report.json'
# Dictionary format: {"alert_type": "Brute Force", "attacker_ips": attacker_ips}
# YOUR CODE HERE:


print("[+] Threat Hunt Complete. Report generated.")
