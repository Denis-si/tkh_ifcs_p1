# CLOUDNANO REMEDIATION PLAN
**Operator:** Dennis
## TOP 5 CRITICAL FIXES
*(From the 20 raw findings, select the 5 that pose the greatest ACTUAL risk. Explain your reasoning.)*

1. **[Unauthenticated AWS S3 Bucket (Contains Customer PII)]**
   * **Justification:** [The exposure of Personally Identifiable Information (PII) represents an immediate legal and reputational disaster. It requires zero technical skill for an attacker to exploit once discovered.]

2. **[SQL Injection in Login Page (Customer Database Portal)]**
   * **Justification:** [This allows attackers to bypass authentication or dump the entire customer database. Since it is a portal, it likely contains sensitive user credentials or financial data.]

3. **[Remote Code Execution in Apache Struts (Internet Facing Web Server)]**
   * **Justification:** [Because it is on an internet-facing server. Unlike the CVSS 10.0 router, which is air-gapped, this can be exploited remotely by anyone on the web to gain full control of the server.]

4. **[SMBv1 Enabled (Internal HR File Server)]**
   * **Justification:** [SMBv1 is the primary vector for ransomware (like WannaCry). While internal, if an attacker gains a foothold elsewhere, they can use this to encrypt the company's HR records.]

5. **[Cross Site Skripting in the Public Support Forum]**
   * **Justification:** [This allows attackers to inject malicious scripts into trusted pages, which then execute in other users browsers.]
