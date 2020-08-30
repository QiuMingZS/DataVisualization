import numpy as np 
import matplotlib.pyplot as plt 


x1 = np.random.normal(30, 2, 100)
x2 = np.random.normal(20, 2, 100)
x3 = np.random.normal(10, 3, 100)

plt.plot(x1, label='curve 1')
plt.plot(x2, label='curve 2')
plt.plot(x3, label='curve 3')

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=8, ncol=3, mode="expand", borderaxespad=0.)
plt.annotate("Important value", (55, 20), xycoords='data', xytext=(5, 33), arrowprops=dict(arrowstyle='->'))

plt.show()