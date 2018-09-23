from numpy import*

#constant definition
h=6.626*1E-34; c=3*1E8; k=1.38*1E-23
a=(2*h*c**2); b=(h*c)/k
e=(2*h)/(c*c); f=h/k

## Blackbody function with respect to wavelength lambda
def blackbody_lam(T,lam):
	return (a/lam**5)*(exp(b/lam*T)-1)**(-1)

## Blackbody function with respect to frequency nu. Caution: before use check this at once

def blackbody_nu(T,nu):
    return (e*nu**3)*(exp(f*nu/T)-1)**(-1)


if __name__=="__main__":
	T=300
	lam=linspace(0.1,30,1000)
	bl=blackbody_lam(T,lam)
	import matplotlib.pyplot as plt
	plt.plot(lam,bl)
	plt.show()

