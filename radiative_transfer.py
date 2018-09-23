##  In this code we take the wavelength range given in Exo_transmit code and generate the Blackbody curve for a particular temperature.
from Blackbody import*
import numpy as np

x=np.loadtxt("default.dat",unpack=True,usecols=0)  ## Here the wavelength is in micrometer

T=600
bl=blackbody_lam(T,x)
import matplotlib.pyplot as plt
plt.plot(x,bl)
plt.show()

