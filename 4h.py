import pandas as pd
import matplotlib.pyplot as plt

# Load iris dataset
df = pd.read_csv("iris.csv")

# Scatter plot to compare two features
plt.figure()
plt.scatter(df["sepal_length"], df["sepal_width"])

# Labels and title
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter Plot: Sepal Length vs Sepal Width")

# Show plot
plt.show()