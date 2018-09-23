##  In this code we take the wavelength range given in Exo_transmit code and generate the Blackbody curve for a particular temperature.
from Blackbody import*
import numpy as np

x=np.loadtxt("default.dat",unpack=True,usecols=0)  ## Here the wavelength is in micrometer

## Loading tempearture profile
tp="isothermal.dat"#raw_input("temperature file=")
l,T=np.loadtxt(tp,unpack=True,usecols=(0,1))

###-- Radiative Transfer Code ---###
""" Here we solve the radiative transfer Equation : dI_n/dz = eps_n - K_n*I_n,
Where I_n is the intensity at emitted from the n-th layer 
	eps_n the emission coefficient,
	K_n   the absorption coefficient of the n-th layer.
	n: most deepest layer of the atmosphere."""
n=len(T)
Intensity=[]
for lam in x:
	B=[]; B=blackbody_lam(T,lam)
	eps=B; k=1 # we take absorption coefficient is 1 and emission is B for LTE.
	for i in range(n):
		I=blackbody_lam(T[i],lam) 
		dIdz=eps[i]-k*I
		I=I+dIdz
	Intensity.append(I)
print len(Intensity)



import matplotlib.pyplot as plt
plt.plot(x,Intensity)
plt.show()
