# OMNI-PORTAL ASSESSMENT REPORT
**Operator:** Denis **Deadline:** May 13 @ 11:59 PM 

## PHASE 1: AUTH BYPASS (SQLi)
* **Payload Used:** [' OR 1=1 --]
* **Result:** Successfully bypassed login and obtained 'SUPPORT_TIER_1_SECRET_TOKEN' cookie.

## PHASE 2: CLIENT-SIDE HIJACK (XSS)
* **Stored XSS Payload:** [<script>alert(document.cookie)</script>]
* **Secret Cookie Captured:** [session_id=admin_secret_99812_do_not_share; auth_token=SUPPORT_TIER_1_SECRET_TOKEN
]

## PHASE 3: API ENUMERATION (BOLA)
* **Insecure Order ID:** [501]
* **Confidential Data Leaked:** [{amount of $15,000.00; confidential server lease order id 501}]

## PHASE 4: THE REMEDIATION
* **Fix for SQLi:** The fix is to use parameterized queries (prepared statements) which the database engine treats the input as data and never executes.
* **Fix for XSS:** Use output encoding which convert special characters into plain text instead of running it.
* **Fix for API BOLA:** The fix is to use Object-Level authorization checks which everytime an API request is made for a specific ID, the server must verify that the user is associated with that order.
