import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle

# Step 1: Load data
df = pd.read_csv('Mall_Customers.csv')

# Step 2: Preprocessing
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
X = df[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Step 3: Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Train KMeans
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

# Step 5: Save model
with open("model.pkl", "wb") as f:
    pickle.dump(kmeans, f)

# Step 6: Save scaler
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Step 7: Save final dataframe with cluster labels
df['Cluster'] = kmeans.labels_
df.to_csv("customer_segments.csv", index=False)

print("✅ Model and scaler saved successfully.")
