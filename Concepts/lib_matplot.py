import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, density=1, facecolor='r', alpha=0.75)

plt.xlabel('Intenll')
plt.ylabel('Proba')
plt.title('Histogram')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(False)
plt.show()

# Ref : https://www.geeksforgeeks.org/python-matplotlib-an-overview/