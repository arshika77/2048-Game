import random

# Rotates a 2D list clockwise
def rotate(grid):
    return list(map(list, zip(*grid[::-1])))

# Implements game logic 
# Generalized for all four directions using rotation logic
def move(grid, dir):

    for i in range(dir): grid = rotate(grid)

    for i in range(len(grid)):

        temp = []

        for j in grid[i]:
            if j != '.':
                temp.append(j)

        temp += ['.'] * grid[i].count('.') 

        for j in range(len(temp) - 1):
            if temp[j] == temp[j + 1] and temp[j] != '.' and temp[j + 1] != '.':
                temp[j] = str(2 * int(temp[j]))
                temp[j + 1] = '.'

        grid[i] = []

        for j in temp:
            if j != '.':
                grid[i].append(j)

        grid[i] += ['.'] * temp.count('.')

    for i in range(4 - dir): grid = rotate(grid)
    
    return grid

# Finds current sum of all the tiles on the grid
def sumTiles(grid):
    sumTile = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] != '.':
                sumTile += int(grid[j][i])

    return sumTile

# Finds empty slot in the game grid
def findEmptySlot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j, 0)
    return (-1, -1, 1)

# Adds a random number to the grid
def addNumber(grid, add_type = 'normal'):
    num = random.randint(1, 2) * 2
    if add_type == 'start':
        for i in range(2):
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            lost = 0
            if grid[x][y] != '.':
                x, y, lost = findEmptySlot(grid)
            if not lost: grid[x][y] = str(num)
    else: 
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        lost = 0
        if grid[x][y] != '.':
            x, y, lost = findEmptySlot(grid)
        if not lost: grid[x][y] = str(num)
    return (grid, lost)

# Prints the current game state
def printGrid(grid):
    print("\n")
    for i in range(len(grid)):
        res = "\t\t"
        for j in range(len(grid[i])):
            for _ in range(5 - len(grid[i][j])): res += " "
            res += grid[i][j] + " "
        print(res)
        print("\n")
    return 0

# Backtracks to a previous state of the game
def backtrack(gridStack, back_count):
    
    for i in range(min(len(gridStack), back_count+1)):
        grid = gridStack.pop()
    gridStack.append(grid)
    return grid, gridStack

