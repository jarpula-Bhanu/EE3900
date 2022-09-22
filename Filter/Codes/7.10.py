import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
n = np.arange(10)
fn=(-1/2)**n
x = np.pad(fn,(0,2),'constant',constant_values=(0))
dftmtx = fft(np.eye(len(x)))
X = x@dftmtx
print(X)