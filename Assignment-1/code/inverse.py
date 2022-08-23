import lcapy as lc
from lcapy.discretetime import z

Xo = z/(z+0.5)
xk = Xo.IZT()
print(xk)

'''
Output:  Piecewise(((-1/2)**n, n >= 0))
'''