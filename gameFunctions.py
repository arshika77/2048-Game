import random
import numpy as np

class Grid2048():
    def __init__(self,dim):
        self.dim = dim
        self.grid = [['0']*self.dim for i in range(self.dim)]
        self.var = [[]*self.dim for i in range(self.dim)]
        self.lost = 0

    # Rotates a 2D list clockwise
    def rotate(self):
        return list(map(list, zip(*self.grid[::-1])))

    # Implements game logic 
    # Generalized for all four directions using rotation logic
    def move(self, dir):

        for i in range(dir): self.grid = self.rotate()

        for i in range(self.dim):

            temp = []

            for j in self.grid[i]:
                if j != '0':
                    temp.append(j)

            temp += ['0'] * self.grid[i].count('0') 

            for j in range(len(temp) - 1):
                if temp[j] == temp[j + 1] and temp[j] != '0' and temp[j + 1] != '0':
                    temp[j] = str(2 * int(temp[j]))
                    temp[j + 1] = '0'

            self.grid[i] = []

            for j in temp:
                if j != '0':
                    self.grid[i].append(j)

            self.grid[i] += ['0'] * temp.count('0')

        for i in range(4 - dir): self.grid = self.rotate()
        
        return self.grid

    # Finds current sum of all the tiles on the grid
    def sumTiles(self):
        sumTile = 0
        for j in range(self.dim):
            for i in range(self.dim):
                if self.grid[j][i] != '0':
                    sumTile += int(self.grid[j][i])

        return sumTile

    # Finds empty slot in the game grid
    def findEmptySlot(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.grid[i][j] == '0':
                    return (i, j, 0)
        return (-1, -1, 1)

    # Randomly initializes the start grid

    # Adds a random number to the grid
    def addNumber(self,add_type,x_cord=None,y_cord=None):
        num = random.randint(1, 2) * 2
        if add_type == 'normal':
            x = random.randint(0, self.dim-1)
            y = random.randint(0, self.dim-1)
            print(x,y)
            if self.grid[x][y] != '0':
                x, y, self.lost = self.findEmptySlot()
            if not self.lost: self.grid[x][y] = str(num)
        elif add_type == 'assign': 
            if self.grid[x_cord][y_cord] != '0':
                x_cord, y_cord, self.lost = self.findEmptySlot()
            if not self.lost: self.grid[x_cord][y_cord] = str(num)

    def play(self,arg_list):
        if self.lost == 1:
            print("Haha Dummy! My grandma plays this game better than you")
        signal = arg_list[0]
        
    # Prints the current game state
    def printGrid(self):
        print("\n")
        for i in range(self.dim):
            res = "\t\t"
            for j in range(self.dim):
                for _ in range(5 - len(self.grid[i][j])): res += " "
                res += self.grid[i][j] + " "
            print(res)
            print("\n")
        return 0


