##  In this code we take the wavelength range given in Exo_transmit code and generate the Blackbody curve for a particular temperature.
from Blackbody import*
import sys,numpy as np


if len(sys.argv)<2:
	print "temperature profile not entered"
	sys.exit(1)
x=np.loadtxt("default.dat",unpack=True,usecols=0)  ## Here the wavelength is in micrometer

print "----------Loading Temperature profile-----"
tp=sys.argv[1]
print "used file:\t",tp
l,T=np.loadtxt(tp,unpack=True,usecols=(0,1))




###-- Radiative Transfer Code ---###
""" Here we solve the radiative transfer Equation : dI_n/dz = eps_n - K_n*I_n,
							    = -K_n*(I_n-S_n)
Where I_n is the intensity at emitted from the n-th layer 
	eps_n the emission coefficient,
	K_n   the absorption coefficient of the n-th layer.
	S_n   Source Function eps_n/k_n
	n=0: most deepest layer of the atmosphere."""
#n=len(T)


Intensity=[]
for lam in x:
	if lam>=5.980389e-01 and lam<=6.205358e-01:
		k=0
	else:
		k=1 # We take absorption coefficient is 1
	I=blackbody_lam(T[0],lam)
	for t in T:
		S=blackbody_lam(t,lam) # for LTE condition
		dIdz=-k*(I-S)
		I=I+dIdz
	Intensity.append(I)
#print len(Intensity)


import matplotlib.pyplot as plt
plt.plot(x,Intensity)
plt.show()
