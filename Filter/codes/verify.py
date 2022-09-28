import numpy as np

x = np.array([2,-1])
h = np.array([-1,2,1])

m = h.shape[0]
n = x.shape[0]

topliz = np.zeros((m+n-1,n))

for i in range(m+n-1):
    for j in range(n):
        if i-j>=0 and i-j<m:
            topliz[i,j] = h[i-j]

y = topliz.dot(x)

#Theoritical
print(f'Theoritical : {y}')

#Using built in function
y_builtin = np.convolve([2,-1],[-1,2,1])
print(f'using built in function : {y_builtin}')
