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
                #move.score += int(temp[j])
                temp[j + 1] = '.'
        grid[i] = []
        for j in temp:
            if j != '.':
                grid[i].append(j)
        grid[i] += ['.'] * temp.count('.')
    for i in range(4 - dir): grid = rotate(grid)
    return grid

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
def addNumber(grid):
    num = random.randint(1, 2) * 2
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

def backtrack(gridStack, back_count):
    
    for i in range(min(len(gridStack), back_count)):
        grid = gridStack.pop()
    return grid, gridStack

# Starts the game
def startGame():
    print("\nWelcome to the 2048 Console world. Let's play!")
    print("Combine given numbers to get a maximum score.\nYou can move numbers to left, right, top or bottom direction.\n")
    
    # Create the game grid 
    # The game should work for square grid of any size though
    
    grid = [['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.']]
    for i in range(2):
        grid, _ = addNumber(grid) #intialize two tiles
    
    gridStack = []
    gridStack.append(grid)
    direction = {'L': 0, 'B': 1, 'R': 2, 'T': 3, 'X': 4}

    printGrid(grid)
    loseStatus = 0
    move.score = 0 # Score of the user
    while True:
        tmp = input("\nTo continue, Press L for left, R for right, T for top, B for bottom or\nPress X to end the game.\n")
        if tmp in ["R", "r", "L", "l", "T", "t", "B", "b", "X", "x"]:
            dir = direction[tmp.upper()]
            if dir == 4:
                print("\nFinal score: " + str(move.score))
                break
            else:
                grid = move(grid, dir)
                grid, loseStatus = addNumber(grid)
                gridStack.append(grid)
                printGrid(grid)
                if loseStatus:
                    print("\nGame Over")
                    print("Final score: " + str(move.score))
                    break
                move.score = sumTiles(grid)
                if(move.score == 8):
                    print("\nFinal score: " + str(move.score))
                    print("\nCongratulations!! You Won")
                    break
                if(move.score>8):
                    print("\nCurrent score: " + str(move.score))
                    back_count = random.randint(1, 3)
                    print("\nScore is greater than 8. Backtracking ... %d moves", min(len(gridStack), back_count))
                    grid, gridStack = backtrack(gridStack, back_count)
                    printGrid(grid)
                    move.score = sumTiles(grid)
                print("\nCurrent score: " + str(move.score))
        else:
            print("\nInvalid direction, please provide valid movement direction (L, B, R, T).")
    return 0

# Program starts here
startGame()

