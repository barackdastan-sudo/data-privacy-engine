import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Privacy Engine", layout="wide")
st.title("🔒 Data Privacy & Anonymization Engine")
st.write("Enterprise-grade PII de-identification and privacy compliance solution.")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.subheader("🔑 Sign In to Continue")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log in"):
        if username == "admin" and password == "AdminPassword123":
            st.session_state["authenticated"] = True
            st.session_state["role"] = "admin"
            st.rerun()
        elif username == "analyst" and password == "AnalystPassword123":
            st.session_state["authenticated"] = True
            st.session_state["role"] = "analyst"
            st.rerun()
        else:
            st.error("Invalid credentials")
else:
    st.sidebar.success(f"Logged in as: {st.session_state['role'].upper()}")
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

    st.subheader("1️⃣ Upload Dataset (CSV)")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        
        # Process Data (Anonymization logic inside dashboard for safety deployment)
        anonymized_df = df.copy()
        if 'Name' in anonymized_df.columns:
            anonymized_df['Name'] = anonymized_df['Name'].astype(str).apply(lambda x: x.split()[0] + "*** " + x.split()[-1] + "***" if len(x.split()) > 1 else x + "***")
        if 'Email' in anonymized_df.columns:
            anonymized_df['Email'] = anonymized_df['Email'].astype(str).apply(lambda x: x.split("@")[0][:2] + "***@" + x.split("@")[-1] if "@" in x else "masked@mail.com")
        if 'Phone' in anonymized_df.columns:
            anonymized_df['Phone'] = anonymized_df['Phone'].astype(str).apply(lambda x: x[:3] + "****" + x[-3:])
        if 'National_ID' in anonymized_df.columns:
            anonymized_df['National_ID'] = "REDACTED-ID"
        if 'Age' in anonymized_df.columns:
            anonymized_df['Age'] = anonymized_df['Age'].apply(lambda x: int(max(18, min(90, x + np.random.laplace(0, 2)))))

        if st.session_state["role"] == "admin":
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("📋 Raw Data (Admin View)")
                st.dataframe(df.head(10))
            with col2:
                st.subheader("🔒 Anonymized Data")
                st.dataframe(anonymized_df.head(10))
        else:
            st.subheader("🔒 Anonymized Data (Analyst View)")
            st.dataframe(anonymized_df.head(10))
            
        csv_data = anonymized_df.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 Download Anonymized CSV", data=csv_data, file_name="anonymized_output.csv", mime="text/csv")
        
        with st.expander("📜 System Audit Logs (Compliance View)"):
            st.text(f"[INFO] User '{st.session_state['role']}' processed dataset and applied Masking & Differential Privacy filters.")
