import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib  # ✅ Use joblib instead of pickle (safer for sklearn models)

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Customer Segmentation", layout="centered")

# ---------- HEADER ----------
st.title("🧠 Customer Segmentation Predictor")
st.markdown("""
Welcome to the **Customer Segmentation App**!  
This tool uses **KMeans clustering** to group customers based on their demographics and shopping behavior.  
It helps businesses understand their customer types and design targeted marketing strategies.
""")

# ---------- FILE CHECK ----------
st.markdown("### 🔍 File Check")
files = os.listdir()
st.write("Current directory files:", files)

if not os.path.exists("model.pkl"):
    st.error("❌ model.pkl not found.")
    st.stop()
else:
    model = joblib.load("model.pkl")
    st.success("✅ model.pkl loaded successfully.")

if not os.path.exists("scaler.pkl"):
    st.error("❌ scaler.pkl not found.")
    st.stop()
else:
    scaler = joblib.load("scaler.pkl")
    st.success("✅ scaler.pkl loaded successfully.")

# ---------- USER INPUT ----------
st.markdown("### 🧾 Enter Customer Details")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 70, 30)
income = st.slider("Annual Income (k$)", 15, 150, 60)
score = st.slider("Spending Score (1-100)", 1, 100, 50)

# ---------- PREDICTION ----------
if st.button("🎯 Predict Customer Segment"):
    gender_encoded = 0 if gender == "Male" else 1
    input_data = np.array([[gender_encoded, age, income, score]])
    input_scaled = scaler.transform(input_data)
    cluster = model.predict(input_scaled)[0]

    st.success(f"✅ Predicted Segment: **Segment {cluster}**")

    # Optional descriptions for each cluster
    cluster_descriptions = {
        0: "🟡 Young & High-Spending Customers",
        1: "🔵 Older Customers with Average Spending",
        2: "🟠 Low Income, Low Spenders",
        3: "🟢 High Income, Moderate Spenders",
        4: "🔴 Mid-age, Average Income & Spending"
    }

    st.info(f"**Segment Description:** {cluster_descriptions.get(cluster, 'No description available')}")

# ---------- FULL DATA ----------
st.markdown("---")
st.markdown("### 📊 View Customer Data with Segments")
if os.path.exists("customer_segments.csv"):
    if st.checkbox("Show full customer dataset"):
        df = pd.read_csv("customer_segments.csv")
        st.dataframe(df)
else:
    st.warning("📁 customer_segments.csv not found.")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("""
📌 **Project:** Customer Segmentation using KMeans  
📁 **Dataset:** [Mall_Customers.csv on Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)  
👩‍💻 **Developed by:** *Mansi Bendale*  
📅 **Internship Project** | July 2025
""")
