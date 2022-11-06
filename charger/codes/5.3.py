import numpy as np
from matplotlib import pyplot as plt
import subprocess
import shlex
from scipy import signal

A = np.loadtxt('resp_butter.txt')
n = 5
fc = 60
b, a = signal.butter(n, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.')
plt.semilogx(f, 20*np.log10(np.abs(h)))
plt.grid()
plt.legend(['Simulation', 'Analysis'])
plt.savefig('../figs/5.3.png')
plt.show()
subprocess.run(shlex.split("termux-open ../figs/5.3.png"))