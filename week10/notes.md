# Week 10 — Digital Forensics, Incident Response (DFIR) & SIEM Log Correlation

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week focused on operating as a Lead Incident Responder to manage the full lifecycle of an enterprise-level breach using advanced Digital Forensics and Incident Response (DFIR) methodologies. The core technical skills involved conducting live host triage to isolate active Command and Control (C2) processes, maintaining an ironclad forensic chain of custody with cryptographic hashing, and parsing unallocated disk sectors using The Sleuth Kit to carve out deleted malware payloads. These offensive-tracking capabilities were fused with enterprise-wide log correlation inside an ELK (Elasticsearch/Kibana) SIEM stack, directly applying the security principles of Continuous Monitoring, Non-Repudiation, and Incident Containment to reconstruct complex, multi-stage attacker timelines.

## Artifacts

* **collection_log.txt** A volatile data triage log capturing real-time network connections, active process identifiers (PIDs) bound to port 4444, and corresponding MD5/SHA256 verification hashes. I generated this file while investigating quarantined containers to capture live system states before they evaporated from memory.
* **forensic_findings.md** A technical threat intelligence document detailing memory-carved strings and disk forensics. I compiled this artifact using low-level file-system tools like `fls` and `icat` to map out deleted file inodes, locate hidden malware beacons in unallocated blocks, and extract hardcoded C2 infrastructure text.
* **attack_timeline.csv** A structured chronological matrix tracking the adversary's lifecycle across the network. I produced this spreadsheet by writing advanced queries in the ELK SIEM stack to aggregate thousands of raw logs, successfully mapping the initial password brute-forcing, lateral movement via compromised Domain Admin accounts, and exact data exfiltration volumes.
* **Incident_Response_Report.md** A comprehensive, capstone Incident Response Report documenting the end-to-end investigation of the TitanCorp network breach. I authored this report for "Operation Phantom Pursuit" to merge SIEM alert validations, host triage data, and raw disk binary extraction into a single, executive-ready defensive briefing.

## Challenges & How I Solved Them

The most significant technical hurdle this week occurred during the data carving phase, where the lab deployment scripts occasionally caused filesystem buffer corruption, leading to incomplete disk synchronization and missing forensic artifacts during recovery validation. I solved this automation flaw by refactoring the deployment shell scripts to integrate low-level kernel disk synchronization mechanisms (`sync`), guaranteeing that volatile filesystem buffers were entirely flushed to disk blocks before analysis began. Additionally, when tracing the attacker's lateral movement inside Kibana, the sheer volume of firewall events created immense background noise; I overcame this by engineering structured search patterns (`enterprise_logs*`) and filtering specifically for anomalous outbound traffic sizes matching the compromised timestamps to pinpoint the data exfiltration vector.

## Reflection

This week's milestones demonstrate that anti-forensic techniques like deleting files or hiding processes only work when a defender relies strictly on standard operating system interfaces. By reaching past OS abstractions to interrogate raw memory and disk sectors, a security practitioner can uncover absolute ground truth. Moving forward, I will focus on optimizing my SIEM query efficiencies and look to incorporate automated alerting rules to flag bulk data exfiltration patterns in real-time before an incident concludes.

## References

* Carrier, B. (2005). *File system forensic analysis*. Addison-Wesley Professional.
* Elastic. (2026). *Kibana guide: Creating data views and analyzing enterprise security logs*. Elastic Documentation. [https://www.elastic.co/guide](https://www.elastic.co/guide)
* Luttgens, J. T., Pepe, M., & Mandia, K. (2014). *Incident response & computer forensics* (3rd ed.). McGraw-Hill Education.
