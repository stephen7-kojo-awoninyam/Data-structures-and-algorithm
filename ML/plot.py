import numpy as np
import matplotlib.pyplot as plt
n = 10
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = np.pi * (60 * np.random.rand(n))**2
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()