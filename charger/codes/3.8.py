import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

A = 12
f = 50

t = np.arange(0,1,1/2000)

x = A*np.abs(np.sin(2*np.pi*f*t))
X = fft(x)
print(X)

N = len(X)
n = np.arange(N)
print(N)

plt.stem(np.real(X),n)
plt.grid()
plt.xlim(-10,10)
plt.ylim(0,10)

plt.show()