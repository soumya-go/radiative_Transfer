##  In this code we take the wavelength range given in Exo_transmit code and generate the Blackbody curve for a particular temperature profile.
from Blackbody import*
import numpy as np
print "\n","#"*5,"welcome","#"*5
print "Reading temperature data.."
##-----Loading tempearture profile-----##

tp="isothermal.dat"#raw_input("temperature file=")
#tp="decreasing_temp.dat"
#tp="incrasing_temp.dat"

print "from",tp,"file"
L,T=np.loadtxt(tp,unpack=True,usecols=(0,1))

print "##"*20

print "reading kappa file..."
###----Reading kappa profile----###

x=[]; k=np.zeros((4616,200))	## here k is a lamda x layer array, where lamda (=4616) is no. of rows & layer (=200) is no. of coloumns.
f=open("kap-250g10h0.dat","r")
A=f.readlines()
c0=0; c1=0
for i in range(len(A)):
	B=A[i].split()
	if len(B)==1:
		lamda=float(B[0])
		x.append(lamda)
		c1=c1+1
	elif len(B)==3:
		l=int(B[0]); kappa=float(B[1]); sigma=float(B[2])
		#if l=L:
		#	print "Error: no. of layer mismatch detected between kappa and Temperature profile."
		c0=c0+1
	if c0!=0:
		k[c1-1][l-1]=kappa
print "done"#k[4615][199]

print "##"*20


print "radiative transfer calculation..."
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
for j in range(len(x)):
	#if x[j]>=5.980389e-01 and x[j]<=6.205358e-01:
	#	k1=0.5
	#else:
	#	k1=1 # We take absorption coefficient is 1

	I=blackbody_lam(T[0],x[j])
	for p in range(len(T)):
		k1=k[j][p]
		S=blackbody_lam(T[p],x[j]) # for LTE condition
		dIdz=-k1*(I-S)
		I=I+dIdz
	Intensity.append(I)
#print len(Intensity)
print "done"

print "##"*20

print "start plotting..."
import matplotlib.pyplot as plt
plt.plot(x,Intensity)
plt.show()
print "done"
