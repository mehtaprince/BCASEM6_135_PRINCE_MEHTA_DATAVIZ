import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

plt.figure()
plt.scatter(df["petal_length"], df["petal_width"])
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()