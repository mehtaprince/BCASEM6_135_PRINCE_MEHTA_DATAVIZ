import pandas as pd

# Read CSV file
df = pd.read_csv("iris.csv")

# Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Take random samples from dataset
sample_data = df.sample(n=10, random_state=42)
print("\nRandom Sample (10 rows):")
print(sample_data)

# Display maximum values of numeric attributes
print("\nMaximum values:")
print(df.max(numeric_only=True))

# Display minimum values of numeric attributes
print("\nMinimum values:")
print(df.min(numeric_only=True))