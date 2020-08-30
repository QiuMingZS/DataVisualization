import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cos_x = np.cos(x)
sin_x = np.sin(x)

plt.plot(x, cos_x, linewidth=4)
line_y, = plt.plot(x, sin_x)
line_y.set_linewidth(7)
plt.setp(line_y, linewidth=0.5)
plt.setp(line_y, marker='p')
plt.setp(line_y, linestyle='-.')
plt.setp(line_y, color='#eeefff')


plt.title("functions $sin(x)$ and $cos(x)$")
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.0, 1.0)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

plt.grid()

plt.show()