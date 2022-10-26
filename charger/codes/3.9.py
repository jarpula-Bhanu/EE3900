import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.05)
y = np.zeros(len(x))
y[40:80] = 1
ffty = np.fft.fft(y)
ffty = np.fft.fftshift(ffty)

plt.plot(np.real(ffty))
plt.plot(np.sinc(x))
plt.xlim(0,80)
plt.ylim(-10,20)
plt.xlabel("f")
plt.ylabel("$\mathcal{F}[rect(t)]$")
plt.legend(['$\mathcal{F}[rect(t)]$','sinc(f)'])
plt.savefig("./figs/3.9.png")
plt.show()