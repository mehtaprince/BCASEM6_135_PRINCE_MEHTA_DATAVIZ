import pandas as pd

df = pd.read_csv("HeightWeight.csv")

# Display first 10 rows
print("First 10 rows:")
print(df.head(10))

# Display last 10 rows
print("\nLast 10 rows:")
print(df.tail(10))

#Display random 20 rows
print("\nRandom 20 rows:")
print(df.sample(20, random_state=42))