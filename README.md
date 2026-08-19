# 🔒 Data Privacy & Anonymization Engine

An enterprise-grade Data Privacy and De-identification solution built with Python. This application allows organizations to safely anonymize Personally Identifiable Information (PII) before performing data analysis, fully complying with the **Data Protection Act**.

## 🚀 Live Demo
Experience the live application here: 
👉 **https://streamlit.app**

## 🛠️ Key Features
- **Role-Based Access Control (RBAC):** Secure login interface separating roles. `Admin` retains full visibility, while `Analyst` only accesses anonymized datasets.
- **Data Masking & Redaction:** Automatically sanitizes sensitive strings like Names, Phone numbers, Emails, and National IDs.
- **Differential Privacy (IBM Diffprivlib):** Injects mathematical Laplace noise into numerical metrics (e.g., Age) to prevent individual re-identification.
- **Compliance Audit Logging:** Chronologically tracks all data processing actions for compliance auditing.

## 🛡️ CyberSecurity & CIA Triad Compliance
- **Confidentiality:** Enforced via dynamic data masking and cryptographic structures.
- **Integrity:** Maintained through an unalterable system audit logging framework.
- **Availability:** Deployed on highly available secure cloud infrastructure with full HTTPS encryption.

## 📦 Tech Stack
- **Frontend:** Streamlit
- **Backend Architecture:** FastAPI / Python 3
- **Data Science Libraries:** Pandas, NumPy, Diffprivlib

