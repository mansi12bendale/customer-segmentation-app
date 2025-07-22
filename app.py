import os
import streamlit as st

st.write("🔍 Files in current directory:", os.listdir())

# Then attempt to load model/scaler
import pickle

if not os.path.exists("model.pkl"):
    st.error("❌ model.pkl not found in the directory")
else:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
        st.success("✅ model.pkl loaded successfully")

if not os.path.exists("scaler.pkl"):
    st.error("❌ scaler.pkl not found in the directory")
else:
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
        st.success("✅ scaler.pkl loaded successfully")
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="Customer Segmentation", layout="centered")

# ---------- HEADER ----------
st.title("🧠 Customer Segmentation Predictor")
st.markdown("""
Welcome to the **Customer Segmentation App**!  
This tool uses **KMeans clustering** to group customers based on their demographics and shopping behavior.  
It helps businesses understand their customer types and design targeted marketing strategies.
""")

# ---------- USER INPUT ----------
st.markdown("### 🔍 Enter Customer Details")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 70, 30)
income = st.slider("Annual Income (k$)", 15, 150, 60)
score = st.slider("Spending Score (1-100)", 1, 100, 50)

# ---------- PREDICT ----------
if st.button("🎯 Predict Customer Segment"):
    gender_encoded = 0 if gender == "Male" else 1
    input_data = np.array([[gender_encoded, age, income, score]])
    input_scaled = scaler.transform(input_data)
    cluster = model.predict(input_scaled)[0]

    st.success(f"✅ The customer belongs to: **Segment {cluster}**")

    # Optional: Add meaning to each cluster
    cluster_descriptions = {
        0: "🟡 Young & High-Spending Customers",
        1: "🔵 Older Customers with Average Spending",
        2: "🟠 Low Income, Low Spenders",
        3: "🟢 High Income, Moderate Spenders",
        4: "🔴 Mid-age, Average Income & Spending"
    }

    description = cluster_descriptions.get(cluster, "No description available.")
    st.info(f"**Segment Description:** {description}")

# ---------- SHOW DATA ----------
st.markdown("---")
st.markdown("### 📊 Full Dataset with Predicted Clusters")
if st.checkbox("Show full customer data"):
    df = pd.read_csv("customer_segments.csv")
    st.dataframe(df)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("""
📌 **Project:** Customer Segmentation using KMeans  
📁 **Dataset:** [Mall_Customers.csv from Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)  
🧑‍💻 **Developed by:** *Mansi Bendale*  
🕒 **Internship Project** | July 2025
""")
