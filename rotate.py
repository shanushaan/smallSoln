myArray = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
            [13,14,15,16],
           [17,18,19,20]]

rotated = zip(*myArray[::-1])
rotated = zip(*rotated[::-1])
rotated = zip(*rotated[::-1])

print rotated


"""
# set looping and condn vars correctly. 
        if (direction ==1): # clockwise
            compare = row_start
            col_index = col_len-len(matrix[0])-1
            rev_row_loop_start = row_len
            rev_row_loop_end = row_start
            
        else: # anticlockwise # 
            compare = row_len-1
            col_index = col_start
            rev_row_loop_start = row_len-1
            rev_row_loop_end = row_start-1
        

"""
"""
if (direction ==1): # clockwise
            row_compare = row_start
            col_id = col_len-len(matrix[0])-1
            row_loop_range = range (row_len,row_start,-1)
            row_rev_compare = row_len
            col_loop_range = range (col_len-1,col_start-1,-1)
            rev_col_id = col_start
        else:
            row_compare = row_len-1
            col_id = col_start
            row_loop_range = range (row_len-1,row_start-1,-1)
            row_rev_compare = row_start
            col_loop_range = range (col_len,col_start,-1)
            rev_col_id = col_len
    

"""
