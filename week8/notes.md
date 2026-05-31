# Week 8 — Exploitation, Privilege Escalation & Lateral Movement

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week focused on executing advanced penetration testing methodologies to understand how adversaries establish initial access, elevate system privileges, and maneuver laterally within segmented enterprise networks. The core technical skills involved weaponizing legacy service vulnerabilities (such as CVE-2007-2447) via Metasploit, exploiting Linux configuration flaws using GTFOBins techniques, and architecting multi-tier network pivots using SOCKS5 proxies and routing tables. These activities directly illustrated the critical security principle of Defense in Depth, proving that securing the perimeter is insufficient if an internal asset lacks hard access controls, strict ingress filtering, and monitored privilege boundaries.

## Artifacts

* **exploit_verification.png** A visual forensic capture validating initial access exploitation. It documents the successful execution of the Samba Usermap Script exploit via Metasploit, confirming an unauthenticated remote root shell on the target system.
* **escalation_path.txt** A technical documentation file detailing the local privilege escalation vectors used to bypass shell restrictions. I compiled this to map out the exact mechanics of utilizing a misconfigured `/usr/bin/find` binary alongside a cron job wildcard injection payload targeting a root-level `tar` command.
* **pivot_success.png** An engineering screenshot capturing live evidence of successful lateral movement and network routing redirection. It proves that local tools like `proxychains` were successfully communicating with an isolated private subnet through an established Meterpreter session.
* **Deep_Pivot_Report.md** A comprehensive After-Action Report detailing the full attack lifecycle for "Operation Deep Pivot." I authored this document to map the entire chain from the initial footholds and persistence scripts down to the discovery and interrogation of an isolated Redis database running on port 6379 deep within the internal network.

## Challenges & How I Solved Them

The most severe technical obstacle this week occurred during the pivoting phase, where my external enumeration tools failed to reach the isolated internal host (`10.0.10.50`) despite having a stable Meterpreter session on the dual-homed compromise vector. I diagnosed this as a routing mismatch caused by a protocol misalignment between the Metasploit routing tables and my local `proxychains` proxy setting, which was dropping standard SOCKS4a DNS queries. I resolved this bottleneck by refactoring the configuration to implement a dedicated SOCKS5 proxy module, updating the local proxychains configuration file to enforce absolute routing parity, and explicitly setting my tool parameters to route entirely through the newly bridged tunnel.

## Reflection

This week's milestones demonstrate that privilege escalation and lateral movement are where real architectural weaknesses are exposed. Gaining an initial foothold is only the first step; understanding how an attacker leverages a single weak node to compromise an entire internal directory or database cluster is what drives effective, defensive network design. Moving forward, I realize the absolute necessity of auditing administrative binaries (`sudo -l`) and will prioritize implementing automated privilege-checking routines within server provisioning baselines.

## References

* Long, J., Gardner, B., & Brown, J. (2016). *Google hacking for penetration testers*. Syngress.
* Messier, R. (2021). *CEH v11 Certified Ethical Hacker study guide*. John Wiley & Sons.
* OffSec. (2025). *GTFOBins: Curated list of Unix binaries that can be used to bypass local security restrictions*. [https://gtfobins.github.io](https://gtfobins.github.io)
