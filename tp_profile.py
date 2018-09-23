###--- Generate Temperature profile for radiatve_transfer code ---###


## Generating Isothermal Temperature profile  ##
fl=open("isothermal.dat","w+")
##fl.write("layer_no.\ttemperature")

n=70 # No. of atmospheric Layers
for i in range(n):
	print>>fl,i,"\t",300
fl.close()
