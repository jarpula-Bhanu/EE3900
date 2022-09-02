import numpy as np
from scipy.fft import fft,ifft
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def nlgn(n,a):
    return a*n*np.log2(n)

x = 2**(np.arange(20))
y1 = np.loadtxt('fft.txt',dtype='double')
y2 = np.loadtxt('ifft.txt',dtype='double')

popt, pcov = curve_fit(nlgn,x,y2)
y2pred = nlgn(x,*popt)

plt.plot(x,y1,'o')
plt.plot(x,y2,'o')
plt.plot(x,y2pred)
plt.legend({'Simulated (FFT)','Simulated (IFFT)','Analysis'})
plt.xlabel("n")
plt.ylabel('T(n)(ms)')
plt.grid()

plt.savefig('../figs/6.7.1_plot.png')
plt.show()