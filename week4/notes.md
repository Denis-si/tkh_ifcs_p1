# Week 4 — Containerization & Secure Deployment

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week focused on designing, deploying, and auditing secure containerized application environments to drastically minimize an application's attack surface. The core technical skills involved leveraging Docker and Docker Compose to build multi-tier infrastructures, enforcing strict frontend/backend network segmentation, and constructing air-gapped malware sandboxes using host-only networking. These tasks directly put into practice the security principles of Isolation, Attack Surface Reduction, and Defense in Depth, proving how container boundaries can contain threats and eliminate attacker persistence.

## Artifacts

* **deploy_web.sh** An automated Bash script built to rapidly provision and tear down ephemeral, disposable Docker web servers. I engineered this tool to ensure pristine, baseline deployment states and completely mitigate persistence risks from potential container compromises.
* **docker-compose.yml** A multi-container infrastructure blueprint defining a segmented application stack. I configured this file with distinct, isolated frontend and internal backend networks to ensure sensitive database services remain completely restricted from direct internet exposure.
* **sandbox_report.txt** A validation report verifying the integrity and containment controls of a custom, host-only malware analysis sandbox. I generated this by executing network egress tests to prove absolute isolation from external production networks.
* **hyperstack_audit.json** A structured configuration audit report evaluating the containerized environment against security benchmarks. I compiled this JSON data to detail the verification of restricted outbound connectivity, user privileges, and active network boundary rules.

## Challenges & How I Solved Them

A major hurdle arose when configuring the multi-container architecture in `docker-compose.yml`, where the backend database container initially failed to communicate with the frontend application. Upon troubleshooting, I discovered an architecture and network isolation conflict where the services were placed on completely separate networks without an explicit bridge routing mechanism for authorized traffic. I resolved this by refactoring the network configuration block to implement strict, multi-homed segmentation—allowing the frontend container to securely bridge into the backend network while keeping the backend completely shielded from the public internet interface.

## Reflection

This week's milestones demonstrate that containerization is an incredibly powerful tool for threat containment when configured with a security-first mindset. It highlighted that default container settings are rarely secure, and a practitioner must proactively enforce network boundaries and resource isolation to prevent container escape or lateral movement. Moving forward, I want to explore automated linting tools to systematically scan configuration files for privilege escalation vulnerabilities before deployment.

## References

* Docker Documentation. (2026). *Networking in Docker Compose*. Docker Docs. [https://docs.docker.com](https://docs.docker.com)
* Ferguson, J. (2020). *Docker security: Enterprise-grade container security principles*. O'Reilly Media, Inc.
* Rice, A. (2023). *Container Security: Fundamental Technology Security that Anyone Who Manages, Uses, or Builds Containers Should Know*. O'Reilly Media, Inc.
