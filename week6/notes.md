# Week 6 — Systems Troubleshooting, Diagnostics & Infrastructure Hardening

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week focused on synthesizing advanced system troubleshooting, container orchestration, and comprehensive infrastructure hardening into a cohesive, production-ready defense model. The core technical skills involved executing multi-layer OSI diagnostic pipelines (spanning Layers 3, 4, and 7) using tools like `ss` and `nc`, orchestrating network-segmented Docker Compose stacks, and authoring a professional Security Architecture Document (SAD). These tasks directly enforced the security principles of Attack Surface Reduction, Least Privilege, and Secure Configuration Management, demonstrating how to eliminate configuration drift and withstand active operational failures.

## Artifacts

* **readiness_check.log** A comprehensive diagnostic and remediation log detailing the structured, OSI-model troubleshooting vectors used to resolve multi-layer system failures. I generated this file while isolating port allocation conflicts, correcting Docker runtime failures, and fixing broken Uncomplicated Firewall (UFW) rules.
* **practical_exam_report.txt** A detailed engineering report capturing the exact command-line methodologies used during a timed incident response simulation. I produced this artifact to document the rapid discovery of root-owned logs via the `find` utility and the immediate enforcement of read-only access controls (`chmod 444`).
* **HardenedOutpost_SAD.pdf** A formal, professional-grade Security Architecture Document mapping out the newly deployed infrastructure blueprint. I authored this document to articulate my technical decisions regarding SSH root disablement, default-deny firewall postures, containerized network segmentation, and custom Python-based system auditing routines.

## Challenges & How I Solved Them

The primary technical bottleneck this week involved a cascading port allocation failure where a newly deployed containerized Nginx stack refused to bind to its designated host port, rendering the backend service inaccessible over Layer 7. I used a structured, bottom-up troubleshooting methodology to isolate the issue: I ran `ss -tulnp` to audit active sockets and uncovered a conflicting, orphaned Docker container silently holding the port reservation. I resolved the collision by systematically pruning the dead container, refactoring the `docker-compose.yml` network blocks to enforce strict internal segmentation, and configuring host-level UFW rules to explicitly permit outward-facing web traffic while dropping unmapped internal queries.

## Reflection

This week's rigorous capstone exercises prove that structural hardening is completely ineffective without an equal capacity for deep-dive system diagnostics. A true security professional must understand how application runtimes interact with network sockets and host operating systems to effectively defend them. Moving forward, I recognize that manually validating host security baselines is inefficient, and I plan to transition my custom Python monitoring tools into continuous configuration compliance scripts.

## References

* Barrett, D. J., Silverman, R. E., & Byrnes, R. G. (2023). *SSH, The Secure Shell: The definitive guide* (2nd ed.). O'Reilly Media, Inc.
* Hockenhull, J. (2020). *Linux system administration recipes: A problem-solution approach*. Apress.
* Ward, B. (2021). *How Linux works: What every superuser should know* (3rd ed.). No Starch Press.
