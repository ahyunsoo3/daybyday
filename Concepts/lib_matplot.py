import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,5)
y = x**5
plt.plot([10,20,30,40],[400,200,300,400],'go',x,y,'r^') # matched with each other.
plt.title('first plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
    

# Ref : https://www.geeksforgeeks.org/python-matplotlib-an-overview/