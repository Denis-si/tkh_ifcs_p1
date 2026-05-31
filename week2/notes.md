# Week 2 — Networking & OSI Operations

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week focused on diagnosing, isolating, and remediating complex network infrastructure failures by systematically troubleshooting issues across multiple layers of the OSI model. The core technical skills involved executing CIDR subnet analysis, manually reconstructing corrupted routing tables, and performing packet-level forensic verification. These exercises directly reinforced the security principles of availability, data integrity, and defense-in-depth, demonstrating how misconfigurations or active network exploits (such as DNS poisoning) can cripple an organization's communication fabric.

## Artifacts

* **briefing.txt** A high-level summary report detailing the initial state of the network outage and the tactical steps taken during the recovery process. I created this to provide clear, executive-level documentation of the incident scope and final resolution.
* **subnet_blueprint.txt** A technical document detailing the exact CIDR corrections, network boundary recalculations, and gateway mappings needed to resolve overlapping subnets. I produced this by analyzing the broken network topology and manually recalculating IP allocations.
* **protocol_audit.txt** A focused security log capturing the results of an investigation into DNS tampering, including a thorough audit of `/etc/hosts` and domain resolution paths. I generated this by verifying local translation files against authorized upstream nameservers to identify poisoning attempts.
* **tlab_report.txt** A comprehensive, end-to-end engineering report documenting the full network restoration, complete with packet capture evidence verifying the successful completion of the TCP three-way handshake. I produced this artifact by capturing live traffic streams to prove stable, authenticated communication was restored.

## Challenges & How I Solved Them

The primary challenge this week was dealing with a multi-layered network outage where issues at the network layer masked separate, underlying issues at the application layer. For example, after fixing the downed interfaces and recalculating the subnet boundaries, external traffic still failed due to a hidden DNS poisoning exploit. I solved this by adopting a rigid, bottom-up troubleshooting methodology—verifying physical and data link stability before moving up to validate routing tables, and finally auditing local hostname resolution files to root out the malicious DNS entries.

## Reflection

This week's lab proved that network security cannot exist without a deep, operational understanding of network engineering. It underscored that packet captures and traffic analysis don't just tell you *if* a network is working, but *how* securely it is performing. In future network incidents, I would immediately run an initial baseline packet capture before making any routing or subnet modifications to preserve the original state of the traffic anomalies.

## References

* Kozierok, C. M. (2005). *The TCP/IP guide: A comprehensive, illustrated Internet protocols reference*. No Starch Press.
* Lammle, T. (2021). *Cisco Certified Network Associate (CCNA) study guide* (Vol. 2). John Wiley & Sons.
* Postel, J. (1981). *Transmission Control Protocol*. Internet Engineering Task Force. RFC 793. [https://datatracker.ietf.org/doc/html/rfc793](https://datatracker.ietf.org/doc/html/rfc793)
