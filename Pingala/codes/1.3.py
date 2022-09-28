import numpy as np

n = 100
roots = np.roots([1,-1,-1])
alpha = roots[0]
beta = roots[1]

k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)

b = a[2:] + a[:98]
b = np.pad(b, (1, 0), 'constant', constant_values=(1, 0))
b_new = alpha**k + beta**k
if (np.allclose(b, b_new[:99])): print("1.3 correct")
else: print("1.3 incorrect")