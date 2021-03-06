import numpy as np 
import matplotlib.pyplot as plt 

mu = 100
sigma = 15
x = np.random.normal(mu, sigma, 10000)

ax = plt.gca()
ax.hist(x, bins=35, color='g')

ax.set_xlabel('Values')
ax.set_ylabel('Frequency')
ax.set_title(r'$\mathrm{Histogram: }\ \mu=%d,\ \sigma=%d$' % (mu, sigma))


plt.show()