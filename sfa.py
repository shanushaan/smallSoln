def melt(yy,ll):
    counter=0
    bb = [0 for index in range(len(ll))]
    while (yy>0):
		inCount=0
		for item in xrange(len(ll)):
			bb[item]+=1
			if ll[item]==bb[item]:
				bb[item]=0
				inCount+=1
		counter+=1
		yy-=inCount
		print inCount,yy
    return counter
print(melt(15,[2,4,3,6]))
