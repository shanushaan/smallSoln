import numpy
def melt(size,pTime):
	print (sorted(pTime))
	counter=0
	pTime = numpy.array(pTime)
	rate = (1./pTime).sum()
	print rate
	counter = int(size/((1./pTime).sum()))
	consumed = (counter // pTime).sum()
	print consumed, len(pTime)
	while consumed < size:
		counter += (pTime - counter % pTime).min()
		
		consumed = (counter // pTime).sum() 
	print consumed
	return counter
	
print(melt(15,[2,4,1,6]))
