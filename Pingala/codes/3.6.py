import numpy as np

n = 100
roots = np.roots([1,-1,-1])
alpha = roots[0]
beta = roots[1]

k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)

# Option 1
ca = np.cumsum(a)
if (np.allclose(ca[:98], a[2:] - 1)): print("option 1 is correct")
else: print("option 1 is incorrect")

z=10
# Option 2
Xz = z**(2)/(z**(2)-z-1)
Xz = Xz/10
ans1 = 10/89
if(np.allclose(Xz,ans1)): print("option 2 is correct")
else : print("option 2 is incorrect")

# Option 3
b = a[2:] + a[:98]
b = np.pad(b, (1, 0), 'constant', constant_values=(1, 0))
b_new = alpha**k + beta**k
if (np.allclose(b, b_new[:99])): print("option 3 is correct")
else: print("option 3 is incorrect")


# Option 4
Yz = (z**(2)+2*z)/(z**(2)-z-1)
Yz = Yz/10
ans2 = 8/89
if(np.allclose(Yz,ans2)): print("option 4 is correct")
else : print("option 4 is incorrect")