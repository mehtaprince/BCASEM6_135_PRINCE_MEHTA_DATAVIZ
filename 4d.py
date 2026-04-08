import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

species_count = df["species"].value_counts()

plt.figure()
plt.bar(species_count.index, species_count.values)
plt.title("Species Frequency - Bar Plot")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()