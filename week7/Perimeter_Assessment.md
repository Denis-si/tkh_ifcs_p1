# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** Dennis
**Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 (172.88.0.10):** nginx 1.14.2
* **Host 2 (172.88.0.15):** Host up (All 1000 scanned ports are in ignored states/closed)
* **Host 3 (172.88.0.20):** Apache httpd 2.4.66 (Unix)

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
* **Web Server 1 Finding:** (172.88.0.10): Server leaks inodes via ETags (header found with file /)
* **Web Server 2 Finding:** (172.88.0.20): No web server found on 172.88.0.15:80 (Scan failed/Target filtered)

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** Outdated Nginx Web Server (Version 1.14.2)
* **Justification:** This version of Nginx (1.14.2) is significantly outdated and likely contains known CVEs; because it is internet-facing, the likelihood of an automated attack is high, and the impact of a potential server compromise outweighs the missing security headers found elsewhere.
