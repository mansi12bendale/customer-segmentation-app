
# 🧠 Customer Segmentation Web App

🚀 **Live App:** [Click here to try the Customer Segmentation App]([https://your-streamlit-link.streamlit.app](https://customer-segmentation-app-297fkmgxxxh3wu4keggphm.streamlit.app/))

---

## 📌 Project Overview

This project is a **Customer Segmentation Web App** built using **Streamlit** and powered by **KMeans Clustering**.

It helps businesses:
- Understand their customer base.
- Group customers into meaningful segments based on behavior.
- Make smarter, targeted marketing decisions.

---

## 🛠️ Features

- 🧍 Gender, Age, Income, and Spending Score input
- 🔍 Real-time segment prediction using a trained KMeans model
- 📊 Display of full customer dataset with assigned clusters
- 💡 Descriptive tags for each customer segment
- 🌐 Deployed on Streamlit Cloud

---

## 📂 Files in This Repo

| File | Description |
|------|-------------|
| `app.py` | Streamlit frontend code |
| `train_model.py` | Script to train and save the clustering model |
| `model.pkl` | Trained KMeans model |
| `scaler.pkl` | Feature scaler for preprocessing input |
| `customer_segments.csv` | Output with cluster labels |
| `Mall_Customers.csv` | Original dataset |
| `requirements.txt` | Required Python packages |
| `.streamlit/` | Streamlit configuration files |
| `README.md` | This file |

---

## 📊 Dataset

- **Source:** [Kaggle - Mall Customer Segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- **Features:**
  - Gender
  - Age
  - Annual Income (k$)
  - Spending Score (1–100)

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/customer-segmentation-app.git

# Navigate to project folder
cd customer-segmentation-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
