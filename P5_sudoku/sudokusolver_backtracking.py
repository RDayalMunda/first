import numpy as np
sudoku = [[0,0,0,0,0,0,6,8,0],
          [0,0,0,0,7,3,0,0,9],
          [3,0,9,0,0,0,0,4,5],
          [4,9,0,0,0,0,0,0,0],
          [8,0,3,0,5,0,9,0,2],
          [0,0,0,0,0,0,0,3,6],
          [9,6,0,0,0,0,3,0,8],
          [7,0,0,6,8,0,0,0,0],
          [0,2,8,0,0,0,0,0,0]]

def chance(x,y,n):
    global sudoku
    ##checkingg vertically
    for i in range(0,9):
        if sudoku[x][i]==n:
            return False
    ##for checcking horizontally
    for i in range(0,9):
        if sudoku[i][y]==n:
            return False
    ##for checking the boxes
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[x0+i][y0+j] == n:
                return False
    return True

def solve():
    global sudoku
    for y in range(0,9):
        for x in range(0,9):
            if sudoku[y][x]==0:
                for n in range(1,10):
                    if chance(y,x,n):
                        sudoku[y][x] = n
                        solve()
                        #sudoku[y][x] = n
                    sudoku[y][x] = 0
                return 
    print(np.matrix(sudoku))
    if input('More?')=='y': 
        solve()
print(np.matrix(sudoku))
print("\ncall the 'solve' function to solve this sudoku")
print("\nTo create you own board. Follow these instruction.\n\t1. create a list of list with your data.\n\t2. Blanks should be replaced by 0's.\n\t3. Assign that list to a variable named 'sudoku'.\n\t4. Now you can call the 'solve' function to solve the solve for you.")

