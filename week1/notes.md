# Week 1 — Linux Security Foundations

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week focused on building core Linux security foundations by executing system enumeration, access control remediation, and log-based threat hunting. The primary technical skills involved navigating the Linux Filesystem Hierarchy Standard (FHS) to locate indicators of compromise and building advanced command-line pipelines to parse system logs. These activities directly connected to the security principles of Least Privilege and Defense in Depth, demonstrating how proper file permissions and continuous monitoring prevent lateral movement and detect active exploits.

## Artifacts

* **discovery.txt** A comprehensive forensic log capturing filesystem reconnaissance, system enumeration data, and hidden secrets extracted during post-exploitation analysis. I generated this by auditing protected system directories and mapping out the environment's structure.
* **threat_ips.txt** A clean, isolated list containing the IP addresses of malicious actors interacting with the system. This was compiled by chaining command-line tools to filter and deduplicate networking logs.
* **final_threat_report.txt** A structured, actionable incident response report summarizing the malicious activities detected within the system logs. I produced this artifact by writing text-parsing pipelines to isolate indicators of compromise (IOCs).
* **harden.sh** An automated Bash script designed to systematically remediate permission vulnerabilities across the OS, such as securing access to `/etc/shadow`. I developed this to streamline system baseline configuration and ensure repeatable security posture enforcement.

## Challenges & How I Solved Them

One of the most significant challenges arose when attempting to isolate specific attacker signatures from massive, cluttered log files, as standard string matching returned overwhelming noise. I solved this by moving beyond basic pattern matching and constructing modular command-line pipelines using `grep`, `awk`, and `sort` to precisely isolate malicious fields. Additionally, dealing with corrupted access controls required careful manipulation of file permissions without locking out critical system processes. I overcame this by methodically mapping out correct absolute permissions before applying automated changes via the hardening script.

## Reflection

This week's work solidifies my understanding of system internals, transforming abstract access control concepts into practical, defensive actions. It proved that a security practitioner must understand baseline system behavior before they can effectively hunt for anomalies or remediate vulnerabilities. Moving forward, I would implement a more robust version-control approach for my automation scripts early in the discovery phase to log incremental changes more cleanly.

## References

* Newlands, J. (2019). *Linux Security Fundamentals*. O'Reilly Media, Inc.
* Shotts, W. (2019). *The Linux command line: A complete introduction* (2nd ed.). No Starch Press.
* The Linux Documentation Project. (2024). *The Linux system administrator's guide*. [https://tldp.org](https://tldp.org)
