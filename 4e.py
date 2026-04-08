import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

species_count = df["species"].value_counts()

plt.figure()
plt.pie(species_count.values, labels=species_count.index, autopct='%1.1f%%')
plt.title("Species Frequency - Pie Chart")
plt.show()