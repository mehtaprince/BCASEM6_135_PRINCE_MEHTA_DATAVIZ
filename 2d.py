import pandas as pd

# Load dataset from CSV file
df = pd.read_csv("HeightWeight.csv")

# Number of observations (rows)
print("Number of observations:")
print(df.shape[0])

# Number of missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# Total number of NaN values in dataset
print("\nTotal NaN values in dataset:")
print(df.isnull().sum().sum())