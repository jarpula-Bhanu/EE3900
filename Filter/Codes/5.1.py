import numpy as np
import matplotlib.pyplot as plt
import scipy

def delta(n):
    if n == 0:
        return 1
    else:
        return 0

def u(n):
    if n >= 0:
        return 1
    else:
        return 0

def h(n):
    return -4*delta(n) + 2*delta(n-1) + 5*u(n)*(-1/2)**n

vec_h = scipy.vectorize(h, otypes=[float])

N = np.linspace(0, 19, 20)
plt.stem(N, vec_h(N))
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.title('Filter Impulse Response')
plt.savefig('../figs/5.1.png')
plt.show()
