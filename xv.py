"""y = [7777,22,3,123,4,122,5,65,23,623,67]
y=[91,1,22,33,44,11,2,21]

for i in range(len(y)):
    for j in range(len(y)):
        if y[j] > y[i]:
            temp = y[i]
            y[i] = y[j]
            y[j] =temp

print y
"""


# Complete the function below.
import itertools

def  derive_comb():
    x = raw_input()
    y = x.split(",")
    #y = [int(item) for item in y]
    lenComb = int(y[len(y)-1])
    if (len(y)-2 < lenComb):
        return[("Error - set size smaller than combination size")]
    
    if (len(y)-2 == lenComb):
        strOut = ",".join(y[:len(y)-2])
        return[ "{"+strOut+"}"]
    sety = set(y[:len(y)-1])
    outlist =[]
    outset = set(itertools.combinations(sety,lenComb))
    #print outset

    outlist =[]
    for item in outset:
        strItem ="{"+ ",".join(item)+"}"
        outlist.append(strItem)
    
    return outlist

xx = derive_comb()
print ",".join(xx)

