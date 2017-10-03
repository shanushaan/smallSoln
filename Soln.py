"""
Started on a wrong note and slowly corrected.
1. Fisrt approach was to loop thorugh seconds untill each of the diskspace has been taken by processes

### It was going to take a very long time for finishing the stuff, so left.###

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
    return counter

2. Tried optimizing 1. by numpy ### But still was going to take a long long time ###

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

3. Studied the problem and with the HINT remembered a puzzle of a car travelling half the distance at 60 and half at 40
gets the avg speed of 48(and NOT 50). ## Because of Rate at which they travel not the distance ##
So tried reasoning with rates at which processes are consuming spaces and set the counter accordingly.

1. Rates are floats so calucaltion comes with float, Time is in seconds =>integer. hence offset of those to be handled.
2. the consumption of space is counted by floor division to get consumed diskspace (<= Time*Sumofrate)

"""

import numpy

# implementation of sum of rates. 
def melt(size,pTime):
        # set variables
	counter=0
	pTime = numpy.array(pTime)
	# mimimum counter time till things are fine (size / (1/(dp1)+1/(dp2) + ....1/(dpn))
	counter = int(size/((1./pTime).sum())) # doing int to check at floor how much diskspace has been used.

        # calculate how much has been used till counter
	consumed = (counter // pTime).sum()

	# if still some space is left. # handle offset.
	while consumed < size:
                # add to counter how much of extra time it may require to get all the disk space occupied
                # i.e. find the mod of current Counter to every process time and getting min of it (say if required 20 sec for next proc to take a byte
                # add 20 directly and use the Counter to get the floor of bytes used).
		counter += (pTime - counter % pTime).min()
                # update totally consumed space.
		consumed = (counter // pTime).sum()
	return counter

def readinput(): # from stdin
    # please input with \n at the end. 
    loopEnd =''
    for line in iter(raw_input,loopEnd):
        array = line.split()
        array = [int(item) for item in array]
        print (melt(array[0],array[1:]))

def readFile(): # from file
    with open('proc_disk_usage.data') as inp:
        for line in inp:
            array= line.split()
            array = [int(item) for item in array]
            print (melt(array[0],array[1:]))
         

# you can call readinput to read via stdin or use readFile to input via file or use both.
#readinput() # uncomment for input from stdin	
readFile()

