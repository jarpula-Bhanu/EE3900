import numpy as np
import scipy
from scipy import fft
from itertools import chain
import timeit
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

def nlgn(n, a): return a*n*np.log2(n)
def nsq(n, a): return a*n*n
def lgn(n, a): return a*np.log2(n);

def pmtx(n):
    col = range(n)
    row = list(chain(range(0, n, 2), range(1, n, 2)))
    data = np.ones(n)
    return scipy.sparse.csr_matrix((data, (row, col)), shape = (n,n))

def id_diag(n):
    w = np.exp(-1j*2*np.pi/n)**(np.arange(n//2))
    Id = scipy.sparse.identity(n//2)
    D = scipy.sparse.dia_matrix((w, [0]), shape=(n//2,n//2))
    return scipy.sparse.bmat([[Id, D], [Id, -D]])


def fftmtx(n):
    if (n == 1): return scipy.sparse.csr_matrix(([1]*1, ([0], [0])), shape=(1,1))
    P = pmtx(n)
    G = fftmtx(n//2)
    M = scipy.sparse.bmat([[G, None], [None, G]])
    L = id_diag(n)
    return L.dot(M).dot(P)

t1 = []
N = 11
x = 1<<np.arange(N)
X = np.arange(2**(N-1)+1)
x_t = np.linspace(10,1001,100)
eps = 1e-6
for i in range(0, N, 1):
    v = np.random.random(size=1<<i)
    st = timeit.default_timer()
    K = fftmtx(1<<i).dot(v)
    en = timeit.default_timer()
    t1.append(1000*(en - st))

a = 2**(np.arange(20))
a1 = np.loadtxt('fft.txt', dtype='double')
a2 = np.loadtxt('ifft.txt', dtype='double')
plt.plot(a, a1, 'o')
plt.plot(a, a2, 'o')
b = np.linspace(1, 2**20 + 1, 2**20)
popt, pcov = curve_fit(nlgn, a, a2)
p1 = nlgn(b, *popt)
plt.plot(b, p1)
popt, pcov = curve_fit(nsq, a, a2)
p2 = nsq(b, *popt)
plt.plot(b, p2)
popt, pcov = curve_fit(lgn, a, a2)
p3 = lgn(b, *popt)
plt.plot(b, p3)
#plots
plt.plot(x, t1, '.')


x1 = np.arange(1e3)
y1 = np.loadtxt('conv.txt',dtype='double')
popt, pcov = curve_fit(nsq , x1, y1)
ypred = nsq(x1,*popt)

plt.plot(x1,y1,'.')
# plt.plot(x1,ypred)

# plt.legend(["Sitmulation (convolution)","Analysis"])
plt.legend(["Simulation (FFT)", "Simulation (IFFT)", "Analysis (n$\log$n)", "Analysis (n$^2$)", "Analysis ($\log$n)","stimulated (Matrix)","Sitmulation (convolution)"])
plt.xlabel('n')
plt.ylabel('T(n) (ms)')
plt.grid()# minor

plt.savefig("../figs/7_11.png")

plt.show()