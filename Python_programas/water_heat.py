import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import fsolve

#670 watts
#1 watt=1 Joule/s
#625 seconds
#418750 Joule

t=np.arange(0,625,1)
Q=670*t
m=1 #1kg/L
T0=2

func = lambda T : Q - m*8.314*(8.712+(T-T0)*1.25/10**3-(T-T0)**2*(0.18/10**6))

Te=np.zeros(np.size(t)+1)
ig = 0
for i in t:
    
    Te[i] = fsolve(func, ig)
   # ig=Te[i]



#def cp(T):
#    a=8.712
#    b=1.25*10**-3
#    c=-0.18*10**-6
#    return 

#Q=mCp(T)
#Q/m=





    

