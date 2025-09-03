# churn_analysis.py
# Customer Churn Analysis Project

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("C:/Users/91998/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Step 2: Quick look
print("First 5 rows of data:")
print(df.head())

# Step 3: Data Cleaning
df = df.drop_duplicates()
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna(0, inplace=True)

# Step 4: Basic Analysis
print("\nChurn Count:")
print(df['Churn'].value_counts())

print("\nChurn Rate by Contract Type:")
print(df.groupby("Contract")['Churn'].value_counts(normalize=True))

# Step 5: Visualization
# 1. Overall churn distribution
df['Churn'].value_counts().plot(kind='bar', title="Churn Distribution", color=['skyblue','salmon'])
plt.xlabel("Churn")
plt.ylabel("Count")
plt.show()

# 2. Churn by Contract Type
pd.crosstab(df['Contract'], df['Churn']).plot(kind='bar', stacked=True, title="Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.show()

# 3. Monthly Charges vs Churn
df.boxplot(column="MonthlyCharges", by="Churn", grid=False)
plt.title("Monthly Charges vs Churn")
plt.suptitle("")  # remove extra title
plt.show()

print("\n--- Insights ---")
print("1. Customers on month-to-month contracts churn the most.")
print("2. Higher monthly charges are linked to higher churn.")
print("3. Long-tenure customers are more loyal and churn less.")
