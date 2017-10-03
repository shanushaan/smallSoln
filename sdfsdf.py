import numpy
def melt(yy,ll):
	counter=0
	bb = numpy.zeros(len(ll,),dtype=numpy.int) 
	ll = numpy.array(ll)
	while (yy>0):
		bb=bb+1
		cc=ll-bb		
		zeroA = numpy.where(cc==0)[0]	
		yy = yy - len(zeroA)
		bb[zeroA] =0
		counter+=1
	return counter
#print(melt(15,[2,4,3,6]))
