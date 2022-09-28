import numpy as np

n = 100
roots = np.roots([1,-1,-1])
alpha = roots[0]
beta = roots[1]

k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)

ca = np.cumsum(a)
if (np.allclose(ca[:98], a[2:] - 1)): print("1.1 correct")
else: print("1.1 incorrect")