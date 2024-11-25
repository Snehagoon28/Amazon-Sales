# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('/Users/sneha/Documents/Python/Amazon sales/Amazon Sale Report.csv')

# Display dataset info
print(df.info())
print (df.columns())
print(df.head())

# Data Cleaning
# Handle missing values
df['Age '] = df['Age '].fillna(df['Age '].median())
df['Gender'] = df['Gender'].fillna('Unknown')
df['PurchaseAmount'] = df['PurchaseAmount'].fillna(df['PurchaseAmount'].median())

# Standardize gender values
df['Gender'] = df['Gender'].replace({'M': 'Male', 'F': 'Female'})

# Convert PurchaseDate to datetime
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

# Remove duplicates
df = df.drop_duplicates()

# Detect and handle outliers in PurchaseAmount
q1 = df['PurchaseAmount'].quantile(0.25)
q3 = df['PurchaseAmount'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df = df[(df['PurchaseAmount'] >= lower_bound) & (df['PurchaseAmount'] <= upper_bound)]

# EDA
# Age distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], kde=True, color='blue')
plt.title('Age Distribution')
plt.show()

# Gender distribution
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8, 6))
gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()

# Top 10 customers by total purchase
top_customers = df.groupby('CustomerID')['PurchaseAmount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_customers.plot(kind='bar', color='orange')
plt.title('Top 10 Customers by Total Purchase Amount')
plt.xlabel('CustomerID')
plt.ylabel('Total Purchase Amount')
plt.show()

# Purchase trends over time
df['PurchaseMonth'] = df['PurchaseDate'].dt.to_period('M')
monthly_trends = df.groupby('PurchaseMonth')['PurchaseAmount'].sum()
plt.figure(figsize=(12, 6))
monthly_trends.plot(kind='line', marker='o', color='purple')
plt.title('Monthly Purchase Trends')
plt.xlabel('Month')
plt.ylabel('Total Purchase Amount')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
