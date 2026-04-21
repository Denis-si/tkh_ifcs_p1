# TITAN SMALL BUSINESS SERVICES: SECURITY ARCHITECTURE DOCUMENT (SAD)
**Operator:** DK
**Date:** 2026-04-21

## 1. Perimeter Hardening (UFW & SSH)
* **SSH Status:** Hardened. Disabled root login and password-based authentication in `/etc/ssh/sshd_config`. Enforced SSH key-pair authentication.
* **Firewall Logic:** Implemented a default-deny policy. Explicitly allowed Port 22 (SSH) for administration and Port 8080 (TCP) for web traffic.

## 2. The Automated Auditor (Python)
* **Script Logic:** 
	'''{=hide}
	'''html
	<pre>
	import os
	from datetime import datetime
	
	hostname = "192.168.1.50" 
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	response = os.system(f"ping -c 4 /{hostname/} > //dev//null")
	
	with open("//var//log//dc_audit.log", "a") as log:
	    if response == 0:
	        log.write(f"[/{timestamp/}] DC is UP\n")
	    else:
	        log.write(f"[/{timestamp/}] DC is DOWN\n")
	</pre>
* **Telemetry Path:** `//var//log//dc_audit.log`

## 3. Containerized App (Docker)
* **Network Isolation:** Used a dual-network strategy. The 'wiki' frontend is on both 'frontend' and 'backend' networks, while the 'db' is isolated on a 'backend' network with internal: true, preventing all direct external access.
* **Stack Health:** 
'''bash 
NAME                IMAGE               STATUS              PORTS
outpost-wiki-1      nginx:latest        Up                  0.0.0.0:8080->80/tcp
outpost-db-1        mysql:latest        Up                  3306/tcp

## 4. Executive Summary
The Hardened Outpost infrastructure is successfully deployed with a multi-layered security posture. Network access is restricted via UFW and key-based SSH, while the application layer utilizes strict network segmentation to air-gap the database from the public internet. Although the Automated Auditor correctly identified the Domain Controller as offline during this session, the system's telemetry and containerized services are fully operational and secure.
