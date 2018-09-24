###--- Generate Temperature profile for radiatve_transfer code ---###

n=70 # No. of atmospheric Layers

p=raw_input("which profile you want(iso/inc./dec.)?")
if p=="iso":
	## Generating Isothermal Temperature profile  ##
	T=input("Enter Isothermal temperature=")
	fl=open("isothermal.dat","w+")
	##fl.write("layer_no.\ttemperature")
	for i in range(n):
		print>>fl,i,"\t",T
	fl.close()
elif p=="dec.":
	fl=open("decreasing_temp.dat","w+")
	T=input("Planet surface Temperature=")
	for i in range(n):
		print>>fl,i,"\t",T
		T-=1
	fl.close()
elif p=="inc.":
	fl=open("incrasing_temp.dat","w+")
	T=input("Planet surface Temperature=")
	for i in range(n):
		print>>fl,i,"\t",T
		T+=1
	fl.close()
