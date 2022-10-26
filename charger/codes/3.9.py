import numpy as np
from scipy import fft, signal
from matplotlib import pyplot as plt
import subprocess
import shlex

ts = 1e-2
sig = np.zeros(200)
sig[:100] = 1
sig_fft = fft.fftshift(fft.fft(sig))
sig_fft = np.abs(sig_fft)/max(np.abs(sig_fft))
sf = fft.fftshift(fft.fftfreq(sig.size, d=ts))
plt.plot(sf, sig_fft, '.')
plt.plot(sf, np.sinc(sf))
plt.legend(['Simulation', 'Analysis'])
plt.grid()
plt.xlabel('f (Hz)')
plt.ylabel('H(f)')
plt.savefig('../figs/3.9.png')
plt.show()
subprocess.run(shlex.split("termux-open ../figs/3.9.png"))