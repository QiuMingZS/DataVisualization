# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *

figure()
x = [1, 2, 3, 4]
y = [5, 4, 3, 2]

subplot(2, 3, 1)
plot(x, y)
subplot(2, 3, 2)
bar(x, y)
subplot(2, 3, 3)
barh(x, y)
subplot(2, 3, 4)
bar(x, y)
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color='r')
subplot(2, 3, 5)
boxplot(x)
subplot(2, 3, 6)
scatter(x, y)

show() 


