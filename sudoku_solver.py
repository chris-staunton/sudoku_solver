
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

def print_grid(grid):
    for row in grid:
        print(row)

def find_empty(grid):
    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            if(grid[row][col] == 0):
                return (row, col)

def valid(row, col, val):
    #row
    for i in range(0,len(grid[row])):
        if(val == grid[row][i]):
            return False

    #col
    for i in range(0,len(grid)):
        if(val == grid[i][col]):
            return False

    #box
    for i in range(row-1,row+1)


def solve(grid):
    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            if(grid[row][col] == 0):
                for num in range(1,10):
                    if(valid(row,col,val)):
                        grid[row][col] = num

                    
                


print_grid(grid)
print(find_empty(grid))

