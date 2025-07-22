# 🧠 Customer Segmentation App

A machine learning web application for **segmenting customers** using **KMeans clustering** based on their age, gender, income, and spending score.

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-success?logo=streamlit)](https://customer-segmentation-app-297fkmgxxxh3wu4keggphm.streamlit.app/)

---

## 📌 Overview

This project helps businesses group customers into distinct clusters using unsupervised machine learning (KMeans) based on demographic and behavioral attributes. It provides a web interface to predict customer segments and view the full clustered dataset.

---

## 📊 Dataset

- **Source**: [Mall_Customers.csv on Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- **Attributes**:
  - Gender
  - Age
  - Annual Income (k$)
  - Spending Score (1–100)

---

## ✨ Features

✅ Predict customer segment using interactive input  
✅ Display dataset with predicted clusters  
✅ Descriptive labels for each cluster  
✅ Clean and responsive Streamlit UI  
✅ EDA notebook included for insights and visualizations

---

## 📈 Exploratory Data Analysis

A detailed EDA is included in the Jupyter notebook:

📄 [EDA_Customer_Segmentation.ipynb](./EDA_Customer_Segmentation.ipynb)

It covers:
- Data distribution
- Correlation matrix
- Elbow method for selecting optimal clusters
- Cluster visualization using PCA

---

## 🚀 Live Demo

Try out the deployed app here:  
👉 **[Launch App on Streamlit](https://customer-segmentation-app-297fkmgxxxh3wu4keggphm.streamlit.app/)**

---

## 🛠️ Run Locally

To run this project on your local machine:

```bash
# Clone the repository
git clone https://github.com/mansi12bendale/customer-segmentation-app.git
cd customer-segmentation-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
