import pandas as pd

# Load dataset
df = pd.read_csv("HeightWeight.csv")

# Shape of dataframe (rows, columns)
print("Shape of DataFrame:")
print(df.shape)

# Size of dataframe (total elements)
print("\nSize of DataFrame:")
print(df.size)

# Datatypes of each column
print("\nData Types of DataFrame:")
print(df.dtypes)