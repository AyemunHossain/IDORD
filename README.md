# 🛡️ IDOR Detector - Automated IDOR Vulnerability Scanner 🔍  

Welcome to **IDOR Detector**, an **automated security tool** designed to detect **Insecure Direct Object Reference (IDOR) vulnerabilities** in web applications and APIs. This tool helps **security researchers, penetration testers, and developers** identify **unauthorized access risks** and **prevent data leaks**.  

---

## 📌 About This Tool  
**IDOR Detector** automates the process of **testing object identifiers** in API requests, checking if they can be **manipulated** to access **restricted** or **sensitive** data.  

💡 **What is IDOR?**  
IDOR occurs when an application **does not properly enforce authorization**, allowing attackers to modify object IDs (e.g., user IDs, file numbers) and gain access to **other users' data**.  

---

## 🚀 Features  
- ✅ **Automated IDOR Scanning** – Detects unauthorized access risks in APIs and web applications.  
- ✅ **Customizable Payloads** – Supports numeric, alphanumeric, and UUID-based identifiers.  
- ✅ **Authenticated Testing** – Allows adding custom **headers and cookies** for testing secured endpoints.  
- ✅ **Smart Fuzzing** – Generates and tests various **object ID variations** dynamically.  
- ✅ **Logging & Reporting** – Saves detailed **scan results** for security auditing.  

---

## ✅ Who This Tool is For?
🔐 Ethical Hackers & Penetration Testers – Identify IDOR vulnerabilities in applications.
👨‍💻 Developers & Security Engineers – Prevent unauthorized data access.
🎯 Bug Bounty Hunters – Automate IDOR testing to find security flaws faster.

---

## Installation

IDORD requires Python3 and pip to run.

Install the dependencies and start the tool.

```sh
pip install -r requirements.txt

#Active the virtual env [varies in linux and windows]

RUN: cd Wrapper 
RUN: python3 IDORD.py
#bang bang
```

