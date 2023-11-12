def corner_corrector(x, y):
    up_down = ""
    left_right = ""
    if x == 0: #top corners
        up_down = 1 #need to go down two rows
    else: #bottom corners
        up_down = -1 #need to go up two rows
    if y == 0: #left
        left_right = 1 #need to go right 2 rows
    else:
        left_right =  -1 #need to go left two rows
    return up_down, left_right

def side_detectors(x, y):
    if x != 1: #up_down side
        return "top_bottom"
    else: #left_right side
        return "left_right"
        
    
    

def validate( block_data ):
    corner_val = (0, len(block_data) - 1)
    for row in range(len(block_data)):
        for column in range(len(block_data[row])):
            if (row in corner_val and column in corner_val) and block_data[row][column] >= 0:
                x, y = corner_corrector(row, column)
                if y < 0:
                  square = block_data[row][column + y:column + 1] + block_data[row + x][column + y:column + 1]
                else:
                  square = block_data[row][column:column + (y * 2)] + block_data[row + x][column:column + (y * 2)] 
                #print(block_data[row][column])
                #print(square)
                #print(square.count(-1))
                if square.count(-1) == block_data[row][column]:
                    pass
                else:
                    return  row, column
            elif ((row in corner_val) ^ (column in corner_val)) and block_data[row][column] >= 0:
                a = side_detectors(row, column)
                if a == "top_bottom":
                    if block_data[1].count(-1) == block_data[row][column]:
                        pass
                    else:
                        return row, column
                else:
                    d = []
                    d.append(block_data[0][1])
                    d.append(block_data[1][1])
                    d.append(block_data[2][1])
                    if d.count(-1) == block_data[row][column]:
                        pass
                    else:
                        return row, column
    return "valid"



                
                
            
            

              
          


grid = [
  [2,-1,2],
  [2,-1,2],
  [1,1,1]
]
print(validate(grid))