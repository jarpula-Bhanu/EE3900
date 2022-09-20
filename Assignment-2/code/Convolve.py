import numpy as np

n = np.random.randint(-1000,1000)
y = 0

if n>=3:
    for k in range(n+1,1000000):
        y = y + 2**(n-k)
else:
    for k in range(4,1000000):
        y = y + 2**(n-k)


print(f"The value of n is : {n}")
print(f"The value of output signal is : {y}")
