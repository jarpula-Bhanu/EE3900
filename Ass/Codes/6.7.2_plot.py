import numpy as np
from scipy.fft import fft,ifft
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def nsq(n,a):
    return a*n*n

x = np.arange(1e3)
y = np.loadtxt('conv.txt',dtype='double')
popt, pcov = curve_fit(nsq , x, y)
ypred = nsq(x,*popt)

plt.plot(x,y,'.')
plt.plot(x,ypred)
plt.xlabel('n')
plt.ylabel('T(n) (s)')
plt.legend(["Sitmulation (convolution)","Analysis"])
plt.grid()

plt.savefig('../figs/6.7.2_plot.png')
plt.show()