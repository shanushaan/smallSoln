# direction = -1 means anticlockwise
# position = 1 means LeftTop, 2 means Right Top, 3 means Right Bottom and 
# 4 means Left Bottom. 

# from the given position spiral should start and as per the given direction either clockwise or anticlockwise
def spiralMatrix(matrix, direction, position):
    # assume tests are done.
    # Thanks will review it.
    # correct the code first. [previous soln is not working with 3*4, 4*3 matrix ]
    # corrected and added direction in the same flow. 
    # now the position problem => seen as we need to transpose the matrix and use that rotated matrix (view) to start the same algo.    

    # rotate the matrix based on position #1 doesnt require change. 
    if position ==2:
        for index in range(3):
            matrix = zip(*matrix[::-1]) # iteratively just transpose the matrix clockwise 3 times to have right top on the start point. 
    elif position ==3:
        for index in range(2):
            matrix = zip(*matrix[::-1]) # same as above just 2 times. 
    elif position ==4:
        matrix = zip(*matrix[::-1]) # just once.
        
    col_len = len (matrix[0])
    row_len = len (matrix)
    row_start =0
    col_start =0

    while (col_len > col_start or row_len > row_start):
        # set the control variables and loop ranges correctly based on direction total 6 places - marked 1-6 
        if (direction ==1): # clockwise
            row_compare = row_start #1 
            col_id = col_len-len(matrix[0])-1 #2
            row_loop_range = range (row_len-1,row_start,-1) #3
            row_rev_compare = row_len-1 #4
            col_loop_range = range (col_len-2,col_start-1,-1)#5
            rev_col_id = col_start #6
        else: #anticlockwise. 
            row_compare = row_len-1 
            col_id = col_start
            row_loop_range = range (row_len-2,row_start-1,-1)
            row_rev_compare = row_start
            col_loop_range = range (col_len-1,col_start,-1)
            rev_col_id = col_len-1
            
        for row in range(row_start, row_len):
            if row == row_compare:  #1
                for col in range (col_start,len(matrix[row])-col_start):    
                    print matrix [row][col],
            else: 
                print matrix [row][col_id],#2

        col_len-=1
        row_len-=1
        
        for row in row_loop_range: #3
            if row == row_rev_compare: #4
                for col in col_loop_range: #5
                    print matrix [row][col],
            else:
                print matrix [row][rev_col_id],#6

        col_start+=1
        row_start+=1

   

myArray = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
            [13,14,15,16],
           [17,18,19,20]]




spiralMatrix(myArray, 1, 2)

# In above case spiral should start from "25" anticlockwise. Printing below:
""""       # The output given is clockwise"""
# 25,20,19,18,17,4,3,2,1,5,9,13,21,22,23,24,16,12,8,7,6,10,14,15,11 => 

# direction = -1 means anticlockwise
# position = 1 means LeftTop, 2 means Right Top, 3 means Right Bottom and 
# 4 means Left Bottom. 
