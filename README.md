# 🧠 Customer Segmentation App

This project performs customer segmentation using **KMeans Clustering** on the popular [Mall_Customers.csv](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) dataset.

The web app is built using **Streamlit**, and allows users to input customer details and predict their segment.

🔗 **Live App**  
👉 [Click here to try the app on Streamlit Cloud](https://customer-segmentation-app-297fkmgxxxh3wu4keggphm.streamlit.app/)

---

## 🚀 Features

- 🎯 Predict customer segment using KMeans model  
- 🧍 Input form for customer demographics (Gender, Age, Income, Spending Score)  
- ✅ Displays predicted segment with description  
- 📊 Option to view full clustered dataset  
- ⚙️ Built with Streamlit for interactive UI

---

## 📁 Project Structure

| File / Folder | Description |
|---------------|-------------|
| `app.py` | Main Streamlit app |
| `train_model.py` | Script to train and save the clustering model |
| `model.pkl` | Saved KMeans model |
| `scaler.pkl` | Saved StandardScaler object |
| `Mall_Customers.csv` | Original dataset |
| `customer_segments.csv` | Data with predicted cluster labels |
| `EDA_Customer_Segmentation.ipynb` | 📝 Full EDA notebook |
| `requirements.txt` | Required Python packages |
| `.streamlit/` | Streamlit config folder |
| `README.md` | This documentation file |

---

## 🔍 Exploratory Data Analysis (EDA)

A complete **EDA notebook** is included in this repository to explore:

- Age, Income & Spending Score distributions  
- Customer demographics  
- Correlation between variables  
- Optimal number of clusters using Elbow method  
- Visualization of clusters (2D and 3D)

📓 [View the EDA notebook](./EDA_Customer_Segmentation.ipynb)

---

## 📦 Installation

### Run locally:

1. Clone the repository:
```bash
git clone https://github.com/mansi12bendale/customer-segmentation-app.git
cd customer-segmentation-app
