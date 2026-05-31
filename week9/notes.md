# Week 9 — Web Application Vulnerabilities, API Security & Chained Exploitation

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned

This week focused on executing comprehensive, full-stack security audits across modern web applications and REST APIs by identifying, weaponizing, and remediating high-impact vulnerabilities from the OWASP Top 10. The core technical skills involved building complex SQL Injection (SQLi) database exfiltration pipelines, crafting Cross-Site Scripting (XSS) session hijacking vectors, manipulating HTTP traffic via Burp Suite to exploit Broken Object Level Authorization (BOLA), and analyzing business logic design flaws. These offensive methodologies directly informed defensive strategies, reinforcing the paramount security principles of Input Sanitization, Output Encoding, Parameterized Queries, and Strict Server-Side Object Authorization.

## Artifacts

* **sqli_report.txt** A technical document detailing database schema mapping and target exploitation mechanics. I compiled this file to record the specific tautology-based authentication bypasses and advanced `UNION SELECT` payloads used to enumerate the `sqlite_master` table and exfiltrate restricted financial records.
* **xss_payloads.txt** An audit log mapping the structure and execution of Reflected/Stored XSS scripts alongside weaponized Cross-Site Request Forgery (CSRF) payloads. I engineered these proof-of-concept scripts to demonstrate active DOM manipulation, administrative cookie theft, and automated, unauthorized background transactions.
* **api_audit.log** A specialized traffic analysis log capturing API endpoint vulnerabilities. I generated this by utilizing Burp Suite to intercept and modify API routing identifiers (ID Swapping) to validate BOLA weaknesses, and tracking automated numerical attacks executed via Burp Suite Intruder to bypass checkout business logic.
* **OmniPortal_Assessment.md** A comprehensive, professional-grade security assessment report summarizing the full chained exploitation of the Titan Omni-Portal. I authored this document to map out the multi-stage attack kill-chain (SQLi to XSS to BOLA) and to provide engineering teams with exact, source-code level secure development remediations.

## Challenges & How I Solved Them

The primary technical bottleneck this week occurred during "Operation Omni-Portal" while attempting to exfiltrate administrative session tokens via Stored XSS, as the application's aggressive backend input parsing kept stripping out standard `<script>` tags, causing the payloads to fail. I resolved this filter evasion challenge by refactoring the malicious strings to bypass basic keyword detection—leveraging alternative HTML event handlers (such as `<img src=x onerror=... >`) and encoding characters to successfully force execution in the browser. Furthermore, when the captured `session_id` cookies could not be used due to an unhandled API-level authorization barrier, I shifted vectors to chain the session theft with a Burp Suite intercept proxy, swapping internal object identifiers to exploit a backend BOLA flaw and successfully complete the exfiltration path.

## Reflection

This week's milestones demonstrate that evaluating vulnerabilities in absolute isolation does not accurately reflect modern web threats. True application security requires understanding how minor, low-severity code anomalies can be chained together by an adversary to create a catastrophic, high-impact exploit chain. Moving forward, I will prioritize advocating for automated static application security testing (SAST) tools within continuous integration pipelines to catch input validation and authorization flaws before code ever hits production.

## References

* OWASP Foundation. (2025). *OWASP Top 10 API security risks and mitigation strategies*. [https://owasp.org](https://owasp.org)
* Stuttard, D., & Pinto, M. (2011). *The Web Application Hacker's Handbook: Finding and exploiting security flaws* (2nd ed.). John Wiley & Sons.
* Sullivan, B., & Liu, V. (2011). *Web 2.0 architectures and common exploitation frameworks*. McGraw-Hill Education.
