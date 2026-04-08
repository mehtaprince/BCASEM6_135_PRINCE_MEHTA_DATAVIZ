import pandas as pd

# Load dataset
df = pd.read_csv("HeightWeight.csv")

# Add new column BMI = Weight / (Height^2)
df["BMI"] = df["Weight"] / (df["Height"] ** 2)

# Display updated dataframe
print(df.head())