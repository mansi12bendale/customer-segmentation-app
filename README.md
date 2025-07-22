# 🧠 Customer Segmentation App

This is a simple Streamlit web application that performs **Customer Segmentation** using **KMeans Clustering**.  
It groups customers based on their gender, age, income, and spending behavior.

👉 **Live Demo**: [Open Streamlit App](https://customer-segmentation-app-297fkmgxxxh3wu4keggphm.streamlit.app/)

---

## 📁 Project Structure

📦 customer-segmentation-app
├── app.py # Streamlit application
├── train_model.py # Script to train KMeans model
├── Mall_Customers.csv # Raw dataset
├── customer_segments.csv # Dataset with cluster labels
├── model.pkl # Trained KMeans model
├── scaler.pkl # Trained StandardScaler
├── requirements.txt # Dependencies
├── EDA_Customer_Segmentation.ipynb # Exploratory Data Analysis notebook
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📊 Dataset

- Dataset: [Mall_Customers.csv](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- Features:
  - `Gender`
  - `Age`
  - `Annual Income (k$)`
  - `Spending Score (1-100)`

---

## 🚀 Features

- Input customer info and predict their segment using KMeans
- Segments customers into 5 clusters
- Displays full dataset with cluster labels
- Helpful visual insights available via EDA notebook

---

## 📈 Exploratory Data Analysis (EDA)

A detailed EDA has been performed and is available in the notebook:

📓 [`EDA_Customer_Segmentation.ipynb`](EDA_Customer_Segmentation.ipynb)

---

## ▶️ Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/mansi12bendale/customer-segmentation-app.git
   cd customer-segmentation-app
Install required dependencies

bash
Copy
Edit
pip install -r requirements.txt
Launch the Streamlit app

bash
Copy
Edit
streamlit run app.py
🙋‍♀️ Developed By
Mansi Bendale
🎯 Internship Project | July 2025

