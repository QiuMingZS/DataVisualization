import matplotlib.pyplot as plt 
import numpy as np 
plt.figure(0)
axes1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
axes2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
axes3 = plt.subplot2grid((3, 3), (1, 2))
axes4 = plt.subplot2grid((3, 3), (2, 0))
axes5 = plt.subplot2grid((3, 3), (2, 1), colspan=2)
all_axes = plt.gcf().axes 
for ax in all_axes:
    for ticklabel in ax.get_xticklabels() + ax.get_yticklabels():
        ticklabel.set_fontsize(6)
y = np.random.randn(12)
ax.plot(y)
plt.suptitle("Demo of subplot2grid")
ax.grid(color='g', linestyle='-', linewidth=0.2)

plt.show()