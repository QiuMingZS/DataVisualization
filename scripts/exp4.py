from pylab import *
ax = gca()
ax.locator_params(tight=True, nbins=10)
ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(10))
ax.plot(np.random.normal(10, .1, 100))

show()