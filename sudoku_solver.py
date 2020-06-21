
grid = [ [0, 0, 0, 0, 0, 8, 0, 3, 0], 
         [0, 2, 0, 0, 3, 0, 0, 4, 0], 
         [0, 0, 0, 0, 0, 6, 5, 2, 0], 
         [0, 0, 0, 0, 6, 0, 0, 0, 0], 
         [0, 4, 0, 3, 0, 1, 8, 0, 5], 
         [5, 0, 7, 0, 4, 0, 9, 0, 0], 
         [0, 0, 3, 0, 1, 4, 0, 0, 0], 
         [1, 7, 4, 0, 0, 0, 0, 5, 0], 
         [0, 0, 0, 0, 2, 0, 0, 0, 0] ]

def print_grid(grid):
    for row in grid:
        print(row)

def find_empty(grid):
    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            if(grid[row][col] == 0):
                return (row, col)

    return None

def valid(grid, pos, val):
    #row
    for i in range(0,len(grid[pos[0]])):
        if(val == grid[pos[0]][i] and pos[1] != i):
            return False

    #col
    for i in range(0,len(grid)):
        if(val == grid[i][pos[1]] and pos[0] != i):
            return False

    #box
    box_y = pos[1] // 3
    box_x = pos[0] // 3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if(val == grid[i][j] and (i,j) != pos):
                return False

    return True

def solve(grid):
   
    find = find_empty(grid)
    if not find:
        print_grid(grid)
        return True

    else:
        row, col = find
        
    for val in range(1,10):
        if(valid(grid, (row, col), val)):
            grid[row][col] = val

            if(solve(grid)):
                return True

            
            grid[row][col] = 0

    return False
                    
                


print_grid(grid)
print("--------------------------")
solve(grid)


