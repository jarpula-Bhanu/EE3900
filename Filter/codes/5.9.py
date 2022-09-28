import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

n = np.arange(14)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

nh=len(h)
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
nx = len(x)

topliz = np.zeros((nx+nh-1,nx))

for i in range(nx+nh-1):
    for j in range(nx):
        if i-j>=0 and i-j<nh:
            topliz[i,j]= h[i-j]
        
y = topliz.dot(x)
print(y)
y1 = linalg.convolution_matrix(x, 6)
print(y1)

#plots
plt.stem(range(0,nx+nh-1),y)
plt.title('Filter Output using Convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

plt.savefig('../figs/5.5_conv.png')
plt.show()
