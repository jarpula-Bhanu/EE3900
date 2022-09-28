import numpy as np

n = 100
roots = np.roots([1,-1,-1])
alpha = roots[0]
beta = roots[1]

k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)

t = 10**k

b = a[2:] + a[:98]
b = np.pad(b, (1, 0), 'constant', constant_values=(1, 0))

tb = b*(1/t[:99])
eps = 1e-6
ans = 8/89
sb = np.cumsum(tb)
if (abs(sb[-1] - ans) < eps): print("1.4 correct")
else: print("1.4 incorrect")