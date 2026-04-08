import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

plt.figure()
plt.hist(df["sepal_length"])
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()