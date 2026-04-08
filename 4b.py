import numpy as np
import matplotlib.pyplot as plt

# Original data
data = np.random.randint(1, 100, 50)

# Add outliers properly
data_with_outliers = np.append(data, [200, 250])

# Box plot
plt.figure()
plt.boxplot(data_with_outliers)
plt.title("Box Plot with Outliers")
plt.show()