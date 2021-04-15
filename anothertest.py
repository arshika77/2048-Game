from copy import deepcopy
import sys
from gameFunctions import Grid2048

game = Grid2048(4)
game.addNumber('normal')
game.var[0][0].append('ABC')
game.var[3][2].append('DEF')
game.var[2][1].append('UVW')
game.var[2][1].append('XYZ')

for i in game.grid:
    for j in i:
        print(j, end = ' ',file = sys.stderr)

for i in range(len(game.var[0])):
    for j in range(len(game.var[0])):
        if game.var[i][j]:
            print("{},{}".format(i,j),end='',file = sys.stderr)
            for tile_name in game.var[i][j]:
                if tile_name != game.var[i][j][len(game.var[i][j])-1]:
                    print("{},".format(tile_name),end='',file = sys.stderr)
                else:
                    print(tile_name,end='',file = sys.stderr)
            print(" ",end='',file = sys.stderr)

