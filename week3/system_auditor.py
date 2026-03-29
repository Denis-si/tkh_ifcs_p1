#!/usr/bin/env python3
import subprocess
import json
import os

print("[*] Initiating System Audit...")

# INSTRUCTION 1: Use subprocess.run() to execute 'ps aux'
# YOUR CODE HERE:
process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)

# INSTRUCTION 2: Search the captured output for the malicious process
# YOUR CODE HERE:
target_process = "unauthorized_cryptominer"
if target_process in process_list.stdout:
	print(f"ALERT: {target_process} detected!")
# INSTRUCTION 3: If found, create a dictionary and save it to 'security_alert.json'
# YOUR CODE HERE:
	alert_data = {
        "event": "Unauthorized Process",
        "severity": "High",
        "process": target_process
	}
	# Instruction 4: Export the alert to a JSON file
	with open("security_alert.json", "w") as file:
        	json.dump(alert_data, file, indent=4)
	print("Security alert generated: security_alert.json")
else:
    print("System audit complete: No unauthorized processes found.")
print("[+] Audit Complete.")
