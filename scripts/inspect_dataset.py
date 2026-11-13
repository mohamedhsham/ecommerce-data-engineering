import pandas as pd

# Load dataset
df = pd.read_csv("data/ecommerce_sales_34500.csv")

# Dataset dimensions
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Column names and data types
print("\nColumn Information:")
print(df.dtypes)

# Preview
print("\nFirst 5 Rows:")
print(df.head())