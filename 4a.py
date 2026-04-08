import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1, 100, 50)

plt.figure()
plt.plot(data)
plt.title("Line Chart")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()

plt.figure()
plt.scatter(range(len(data)), data)
plt.title("Scatter Plot")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()

plt.figure()
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.boxplot(data)
plt.title("Box Plot")
plt.show()