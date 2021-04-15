import random
from copy import deepcopy

class Grid2048():
    def __init__(self,dim):
        self.dim = dim
        self.grid = [['0']*self.dim for i in range(self.dim)]
        self.var = []
        l = []
        for i in range(self.dim):
            l.append([])
        for i in range(self.dim):
            self.var.append(deepcopy(l))
        self.lost = 0

    # Rotates a 2D list clockwise
    def rotate(self, list_type):
        if list_type == 'grid':
            return list(map(list, zip(*self.grid[::-1])))
        elif list_type == 'var':
            return list(map(list, zip(*self.var[::-1])))

    # Implements game logic 
    # Generalized for all four directions using rotation logic
    def move(self, dir, move_type):

        for i in range(dir): 
            self.grid = self.rotate('grid')
            self.var = self.rotate('var')

        for i in range(self.dim):

            temp = []
            temp_var = []
#            l = []
#            for i in range(self.dim):
#                temp_var.append(deepcopy(l))

            for j in self.grid[i]:
                if j != '0':
                    temp.append(j)
            for k in self.var[i]:
                if k != []:
                    temp_var.append(k)

            temp += ['0'] * self.grid[i].count('0')
            l = []
            temp_var += [deepcopy(l) for i in range(self.var[i].count([]))]

            for j in range(len(temp) - 1):
                if temp[j] != '0' and temp[j + 1] != '0':
                    if move_type == 0:
                        temp[j] = str(int(temp[j]) + int(temp[j+1]))
                    temp[j + 1] = '0'
                    temp_var[j].extend(deepcopy(temp_var[j+1]))
                    temp_var[j+1] = deepcopy([])
                if temp[j] == temp[j + 1] and temp[j] != '0' and temp[j + 1] != '0':
                    if move_type == 1:
                        temp[j] = str(0)
                        temp_var[j] = deepcopy([])
                    elif move_type == 2:
                        temp[j] = str(int(temp[j])**2)
                        temp_var[j].extend(deepcopy(temp_var[j+1]))
                    elif move_type == 3:
                        temp[j] = str(1)
                        temp_var[j].extend(deepcopy(temp_var[j+1]))
                        
                    temp[j + 1] = '0'
                    temp_var[j+1] = deepcopy([])
                    
                    
            self.grid[i] = []
            self.var[i] = []

            for j in temp:
                if j != '0':
                    self.grid[i].append(j)
            for k in temp_var:
                if k != []:
                    self.var[i].append(k)

            self.grid[i] += ['0'] * temp.count('0')
            l = []
            self.var[i] += [deepcopy(l) for i in range(temp_var.count([]))]

        for i in range(4 - dir): 
            self.grid = self.rotate('grid')
            self.var = self.rotate('var')

    # Checks the coordinates of the tile
    def checkCord(self,x):
        return x>=0 and x<self.dim

    # Checks if tile name already exists
    def checkName(self,tile_name):
        for i in range(self.dim):
            for j in range(self.dim):
                if tile_name in self.var[i][j]:
                    return False
        return True

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
                if [tile_name] in self.var[i][j]:
                    return (i, j)
        return ("Var Not in Grid")

    # Randomly initializes the start grid

    # Adds a random number to the grid
    def addNumber(self, add_type='normal', info=None):
        num = random.randint(1, 2) * 2
        if add_type == 'normal':
            x = random.randint(0, self.dim-1)
            y = random.randint(0, self.dim-1)
            if self.grid[x][y] != '0':
                x, y, self.lost = self.findEmptySlot()
            if not self.lost: 
                self.grid[x][y] = str(num)
        elif add_type == 0:
            tile_val = info[0]
            x_cord = int(info[1])
            y_cord = int(info[2])
            if not self.checkCord(x_cord) or not self.checkCord(y_cord):
                raise ValueError("Coordinates out of range. Coordinates must be in the range (0,%s) " %self.dim)            
            self.grid[x_cord][y_cord] = str(tile_val)
        elif add_type == 1:
            x_cord, y_cord = self.findVarSlot(info[1])
            if not self.checkCord(x_cord) or not self.checkCord(y_cord):
                raise ValueError("Coordinates out of range. Coordinates must be in the range (0,%s) " %self.dim)
            self.grid[x_cord][y_cord] = str(info[0])
        elif add_type == 2: 
            x_cord_from = int(info[0])
            y_cord_from = int(info[1])
            x_cord_to = int(info[2])
            y_cord_to = int(info[3])
            if not self.checkCord(x_cord_to) or not self.checkCord(y_cord_to)or not self.checkCord(x_cord_from) or not self.checkCord(y_cord_from):
                raise ValueError("Coordinates out of range. Coordinates must be in the range (0,%s) " %self.dim)
            self.grid[x_cord_to][y_cord_to] = self.grid[x_cord_from][y_cord_from]
            
    def assignVarName(self, tile_name, x_cord, y_cord):
        x = int(x_cord)
        y = int(y_cord)
        if not self.checkCord(x) or not self.checkCord(y):
            raise ValueError("Coordinates out of range. Coordinates must be in the range (0,%s) " %self.dim)
        if not self.checkName(tile_name):
            raise ValueError("Cannot name tile. Tile name \"%s\" already exists " %tile_name)
        self.var[x][y].append([tile_name])
        print('2048> Variable {} is currently assigned to coordinates ({},{})'.format(tile_name,x_cord,y_cord))
    
    def query(self, signal, info):
        if signal == 20:
            x_cord = int(info[0])
            y_cord = int(info[1])
            if not self.checkCord(x_cord) or not self.checkCord(y_cord):
                raise ValueError("Coordinates out of range. Coordinates must be in the range (0,%s) " %self.dim)
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
        elif signal == 19:
            info = arg_list[1:]
            self.assignVarName(info[0], info[1], info[2])
        elif signal in range(20, 22):
            info = arg_list[1:]
            val = self.query(signal, info)
            print('2048> Value stored in {} is {}'.format(info, val))
#            for i in range(self.dim):
#                for j in range(self.dim):
#                    if info[0] in self.var[i][j]:
#                        print(i,j)
               
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


