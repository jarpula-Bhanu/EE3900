import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.05)
y = np.sinc(x)
ffty = np.fft.fft(y)
# ffty = np.fft.fftshift(ffty)
# ffty = np.ceil(np.real(ffty))
# print(ffty)

plt.plot(ffty)
# plt.xlim(30,60)
# plt.ylim(-10,20)
plt.xlabel("f")
plt.ylabel("$\mathcal{F}[rect(t)]$")
plt.legend(['$\mathcal{F}[rect(t)]$','sinc(f)'])
plt.savefig("./figs/3.10.png")
plt.show()