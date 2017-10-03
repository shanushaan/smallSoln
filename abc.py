def smallestTrailSum(matrix):
    # assmuming the tests for differnt tests done.
    # find min_sum till [path]

    if not matrix: 
        return None
    if len(matrix) == 0 :
        return None
    
    for row in range(len(matrix)): 
        for col in range(len(matrix[row])): 
            if row ==0 and col ==0: 
                pass
            elif row==0:
                matrix[row][col] += matrix[row][col-1] 
            elif col==0:
                matrix[row][col] += matrix[row-1][col]
            else: 
                matrix[row][col] += min(matrix[row][col-1],matrix[row-1][col])
    print matrix
    return matrix[-1][-1]

myArray = [[1, 2, 3, 4],
             [1, -2, 7, 11],
            [9, 5,7,12]]

print zip(*myArray)[::-1]

#print smallestTrailSum(myArray)


myArray = None
#print smallestTrailSum(myArray)
'''

#
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10,11,12]
# [13,14,15,16]
#  
# Mat(i,j) = Mat(i,j) + min(Mat (i,j-1), Mat (i-1,j))
#
# [1, 3, 6, 10]
# [6, 9, 13, 18]
#
#
# Smallest SUM of trail starting from LT to RB.
# 1 - 2 - 3 -4 - 8 - 12 - 16
# 1 - 2 - 3 - 7 - 8 - 12 - 16
# 1 - 2 - 3 - 7 - 11 - 12 - 16
# 
#
#
# 1 - 5 - 9- 13 - 14 - 15 - 16

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = raw_input()
remove = ["NS", "SN", "EW", "WE"]
removeDict = {"NES":"E","NWS":"W","SWN":"W","SEN":"E", "ENW":"N","ESW":"S","WSE":"S","WNE":"N"}
strReplaced = True
while(strReplaced):
    changed = False
    for item in remove:
        while inp.find(item) != -1:
            inp= inp.replace(item, "")
            changed =True
    for item in removeDict:
        if inp.find(item)!= -1:           
            changed = True
            inp = inp.replace(item,removeDict[item])
    if (changed):
        strReplaced =True
    else:
        strReplaced =False

print "".join(sorted(inp))


