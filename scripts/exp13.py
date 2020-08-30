import matplotlib.pyplot as plt  
from matplotlib import patheffects
import numpy as np 

data = np.random.randn(70)

fontsize = 18
plt.plot(data)
title = "This is the title of the figure"
x_label = "This is the x label"
y_label = "This is the y label"

title_text_obj = plt.title(title, fontsize=fontsize, verticalalignment='bottom')
title_text_obj.set_path_effects([patheffects.withSimplePatchShadow()])

offset = (-1, 1)
rgbRed = (1.0, 0.0, 0.0)
alpha = 0.8 

pe = patheffects.withSimplePatchShadow(offset=offset, shadow_rgbFace=rgbRed, alpha=alpha)

xlabel_obj = plt.xlabel(x_label, fontsize=fontsize, alpha=0.5)
xlabel_obj.set_path_effects([pe])

ylabel_obj = plt.ylabel(y_label, fontsize=fontsize, alpha=0.5)
ylabel_obj.set_path_effects([pe])




plt.show()