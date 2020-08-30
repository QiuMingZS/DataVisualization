import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.randn(1000)
y1 = np.random.randn(len(x))
y2 = 1.2 + np.exp(x)

ax1 = plt.subplot(1, 2, 1)
plt.scatter(x, y1, color='indigo', alpha=0.3, edgecolors='white', label='no correl')
plt.xlabel('no correlation')
plt.grid(True)
plt.legend()

ax2 = plt.subplot(1, 2, 2)
plt.scatter(x, y2, color='green', alpha=0.3, edgecolors='grey', label='correl')
plt.xlabel('strong correlation')
plt.grid(True)
plt.legend()

plt.show()