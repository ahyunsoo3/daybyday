import matplotlib.pyplot as plt
import numpy as np

data = {'a':np.arange(50),
        'c':np.random.randint(0,50,50),
        'd':np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 20

plt.scatter('a','b',c='c',s='d',data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

# Ref : https://www.geeksforgeeks.org/python-matplotlib-an-overview/