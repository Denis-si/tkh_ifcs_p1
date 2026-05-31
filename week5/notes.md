# Week 5 — Enterprise Identity & Active Directory

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week focused on designing, scaling, and defending centralized enterprise identity infrastructures by deploying a Windows Server Active Directory environment and integrating cross-platform systems. The core technical skills involved building an AD forest (`titan.local`), provisioning users via PowerShell automation, enforcing Group Policy Objects (GPOs), and configuring Linux-to-Windows domain integration using Kerberos and SSSD. These tasks directly put into practice the security principles of Centralized Identity Management, Least Privilege, and Policy Enforcement, proving how enterprise-wide security baselines can be universally maintained from a single identity provider.

## Artifacts

* **onboard_engineers.ps1** An automated PowerShell script engineered to bulk-provision domain accounts securely within targeted Organizational Units (OUs). I wrote this utility utilizing the `New-ADUser` cmdlet to ensure standardized, error-free onboarding configurations at scale.
* **onboard_engineers_proof_*.png** A collection of verified cryptographic captures and administrative console screenshots confirming successful, automated user account generation and structured OU mapping within the live domain database.
* **gpo_audit.txt** A structured validation report capturing active security policy application across the network. I generated this file after executing system-level auditing commands (`gpupdate /force` and detailed result parsing) to verify that specific password complexities and access restrictions were explicitly enforced.
* **unified_identity.png** A visual forensic capture confirming successful domain discovery, dynamic Kerberos ticket granting, and Linux authentication integration. It explicitly captures an Ubuntu endpoint authenticating domain users and validating root access mapping via `sssd`.
* **tlab5_report.txt** A comprehensive, capstone enterprise audit report evaluating the operational health and configuration posture of the entire deployment. I produced this artifact to validate structural integrity, policy propagation, cross-platform security, and central group delegation boundaries.

## Challenges & How I Solved Them

Week 5 demanded immense precision, particularly during the cross-platform integration phase where the Linux client consistently failed to discover the Active Directory domain controller. I diagnosed this as a multi-layered configuration failure involving misaligned DNS resolution vectors and out-of-sync system times, which breaks Kerberos authentication handshakes by design. I worked through this barrier by refactoring the Linux endpoint's network configuration to point strictly to the Windows Domain Controller for DNS, syncing the system clocks using NTP, and carefully editing `/etc/sudoers.d/domain_admins` to map AD security groups to local root privileges without compromising terminal access.

## Reflection

This week's milestones highlight that identity is the ultimate perimeter in modern enterprise security architecture. Managing individual endpoints reactively is unviable; a practitioner must know how to scale access control, audit group policies, and centralize permissions globally across disparate operating systems. Moving forward, I recognize the value of implementing stricter auditing on GPO modifications and intend to explore automated monitoring strategies for unauthorized adjustments to central Active Directory groups.

## References

* Microsoft Documentation. (2026). *Active Directory Domain Services overview and Group Policy architecture*. Microsoft Learn. [https://learn.microsoft.com](https://learn.microsoft.com)
* Posey, B. (2023). *Windows Server 2022 & Active Directory administration handbook*. Packt Publishing.
* Red Hat Product Documentation. (2025). *Integrating Red Hat Enterprise Linux and Ubuntu with Active Directory using SSSD and realmd*. Red Hat Customer Portal. [https://access.redhat.com](https://access.redhat.com)
