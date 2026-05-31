# Week 11 — Network Defense & Perimeter Hardening

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week marked a critical transition from offensive exploitation to defensive engineering by designing and deploying a multi-layered, defense-in-depth architecture. The core technical skills involved building a segmented DMZ network architecture using Docker subnets, writing strict egress filtering rules via `iptables`, deploying Suricata with custom intrusion detection signatures, and enforcing system monitoring using SysmonForLinux. These defensive controls directly map to the security principles of Least Privilege, Continuous Monitoring, and Attack Surface Reduction, demonstrating how an enterprise can systematically isolate, detect, and neutralize threat actors at the perimeter, on the wire, and on the endpoint itself.

## Artifacts

* **firewall_config.sh** An automated shell script implementing host-level network defenses using `iptables` and `UFW`. I engineered this file to establish a strict default-deny posture, construct a localized DMZ architecture, and enforce rigorous egress filtering rules that prevent compromised internal containers from establishing unauthorized outbound callbacks to external attacker infrastructure.
* **custom_ids.rules** A collection of customized network security signatures written for the Suricata Intrusion Detection System. I developed these rules to monitor live traffic streams crossing the network bridge, parse payloads for specific indicator strings, and trigger immediate notifications within `fast.log` upon detecting active exploit attempts.
* **edr_policy.xml** A granular Endpoint Detection and Response configuration policy written in XML format for SysmonForLinux. I authored this schema to audit kernel-level system activities, mapping explicit process creation events, suspicious binary execution paths, and rapid file modifications to catch ransomware precursor behavior before encryption begins.
* **Operation_Fortress_Report.md** A comprehensive, professional-grade security architecture report summarizing the engineering execution of the capstone defensive gauntlet. I compiled this document to detail how the network isolation layer, custom IDS sensor, and endpoint logging engine fuse into a single, unified defensive fabric capable of defeating an advanced attack lifecycle.

## Challenges & How I Solved Them

The primary technical bottleneck this week occurred during the integration of the Suricata container with the custom Docker DMZ bridge, where the IDS sensor initially failed to capture traffic moving between the web server and the database, leading to dropped alerts. I diagnosed this as a visibility issue caused by Docker's internal NAT isolation, which prevented the containerized sensor from sniffing the raw interface packets implicitly. I solved this network abstraction challenge by refactoring the container runtime deployment—altering the configuration to attach the Suricata interface directly to the underlying Docker bridge using host networking modes and setting the promiscuous flag via `ip link`, allowing the sensor to successfully inspect every internal packet crossing the subnet wire.

## Reflection

This week's milestones demonstrate that effective cyber defense requires an intimate understanding of the attacker's playbooks. Knowing how an exploit payload behaves on the wire or how ransomware executes in memory allows a practitioner to write high-fidelity signatures and strict access controls rather than relying on generic security configurations. Moving forward, I will focus on optimizing my endpoint rules to ensure that aggressive process monitoring balances robust security logging with real-world system resource utilization.

## References

* Bisson, D. (2022). *Linux firewalls: Enhancing security with iptables and UFW*. No Starch Press.
* Microsoft Corporation. (2026). *System Monitor (Sysmon) configuration guide for Windows and Linux environments*. Microsoft Learn. [https://learn.microsoft.com](https://learn.microsoft.com)
* Open Information Security Foundation. (2025). *Suricata user guide: Writing custom rules and analyzing fast.log outputs*. OISF Docs. [https://docs.suricata.io](https://docs.suricata.io)
