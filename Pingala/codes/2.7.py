import lcapy as lc
from lcapy.discretetime import z

Yz = (z**(2)+2*z)/(z**(2)-z-1)
yn = Yz.IZT()
print(yn)