from pylab import *
dataset = [113, 115, 119, 121, 124, 
           124, 125, 126, 126, 126, 
           127, 127, 128, 129, 130, 
           130, 131, 132, 133, 136]
subplot(1, 2, 1)
boxplot(dataset, vert=False)

subplot(1, 2, 2)
hist(dataset)

show()