import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("tips.csv")

# Scatter Plot
plt.figure()
plt.scatter(df["total_bill"], df["tip"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Scatter Plot")
plt.show()

# Line Chart
plt.figure()
plt.plot(df["total_bill"], df["tip"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Line Chart")
plt.show()

# Bar Chart
plt.figure()
plt.bar(df["day"], df["total_bill"])
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Bar Chart")
plt.show()

# Histogram
plt.figure()
plt.hist(df["total_bill"])
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()