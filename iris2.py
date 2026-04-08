import pandas as pd

# Read dataset
df = pd.read_csv("iris_full.csv")

# Count records for each class (species)
class_count = df["species"].value_counts()

# Display result
print("Number of records for each class:")
print(class_count)