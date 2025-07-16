import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(size=100)
plt.hist(x, bins=10)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Random Normal Data")
plt.show()