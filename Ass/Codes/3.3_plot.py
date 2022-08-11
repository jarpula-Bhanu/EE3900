import matplotlib.pyplot as plt
import numpy as np
k = 20 

y = np.loadtxt("3.3.dat")
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

plt.savefig('../figs/3.3_plot.png')
plt.show()