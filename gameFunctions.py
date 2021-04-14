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
    def move(self, dir, move_type):

        for i in range(dir): self.grid = self.rotate()

        for i in range(self.dim):

            temp = []

            for j in self.grid[i]:
                if j != '0':
                    temp.append(j)

            temp += ['0'] * self.grid[i].count('0') 

            for j in range(len(temp) - 1):
                if temp[j] == temp[j + 1] and temp[j] != '0' and temp[j + 1] != '0':
                    if move_type == 0:
                        temp[j] = str(2 * int(temp[j]))
                    elif move_type == 1:
                        temp[j] = str(0)
                    elif move_type == 2:
                        temp[j] = str(int(temp[j])**2)
                    elif move_type == 3:
                        temp[j] = str(1)
                    
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
    
    def findVarSlot(self, tile_name):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.var[i][j] == tile_name:
                    return (i, j)
        return ("Var Not in Grid")

    # Randomly initializes the start grid

    # Adds a random number to the grid
    def addNumber(self, add_type='normal', info=None):
        num = random.randint(1, 2) * 2
        if add_type == 'normal':
            x = random.randint(0, self.dim-1)
            y = random.randint(0, self.dim-1)
            print(x,y)
            if self.grid[x][y] != '0':
                x, y, self.lost = self.findEmptySlot()
            if not self.lost: 
                self.grid[x][y] = str(num)
        elif add_type == 0:
            tile_val = info[0]
            x_cord = info[1]
            y_cord = info[2]
            self.grid[x_cord][y_cord] = str(tile_val)
        elif add_type == 1:
            x_cord, y_cord = self.findVarSlot(info[1])
            self.grid[x_cord][y_cord] = str(info[0])
        elif add_type == 2: 
            x_cord_from = info[0]
            y_cord_from = info[1]
            x_cord_to = info[2]
            y_cord_to = info[3]
            self.grid[x_cord_to][y_cord_to] = self.grid[x_cord_from][y_cord_from]
            
    def assignVarName(self, tile_name, x_cord, y_cord):
        self.var[x_cord][y_cord] = tile_name
    
    def query(self, signal, info):
        if signal == 20:
            x_cord = info[0]
            y_cord = info[1]
        else:
            x_cord, y_cord = self.findVarSlot(info[0])
        return self.grid[x_cord][y_cord]

    def play(self,arg_list):
        
        signal = arg_list[0]
        if signal in range(16):
            move_type = (signal-(signal%4))/4
            self.move(signal%4, move_type)
            self.addNumber()
        elif signal in range(16, 19):
            info = arg_list[1:]
            self.addNumber(signal%16, info=info)
        elif signal is 19:
            info = arg_list[1:]
            self.assignVarName(info[0], info[1], info[2])
        elif signal in range(20, 22):
            info = arg_list[1:]
            val = self.query(signal, info)
            print('Value stored in {} is {}'.format(info, val))
        
        if self.lost == 1:
            print("Haha Dummy! My grandma plays this game better than you")
                       
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


