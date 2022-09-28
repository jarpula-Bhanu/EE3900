import lcapy as lc
from lcapy.discretetime import z

Xz = z**(2)/(z**(2)-z-1)
xn = Xz.IZT()
print(xn)
