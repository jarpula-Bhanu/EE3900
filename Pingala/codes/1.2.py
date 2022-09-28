import numpy as np

n = 100
roots = np.roots([1,-1,-1])
alpha = roots[0]
beta = roots[1]

k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)

t = 10**k
ta = a*(1/t)
eps = 1e-6
ans = 10/89
sa = np.cumsum(ta)
if (abs(sa[-1] - ans) < eps): print("1.2 correct")
else: print("1.2 incorrect")