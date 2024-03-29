from lexer import Lexer
from parsetrans import Parser
import sys
from gameFunctions import Grid2048

def print_to_stderr(flagVal):
    print("2048> STDERR OUTPUT: ",end='',file = sys.stderr)
    if flagVal == 0:
        for i in game.grid:
            for j in i:
                print(j, end = '\40',file = sys.stderr)

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
        
        print("\n",file=sys.stderr)
    else:
        print(-1,end='',file=sys.stderr)
        print("\n",file=sys.stderr)

game = Grid2048(4)
game.addNumber('normal')

print("2048> Welcome to the 2048-game engine @DevelopedBy Arshika ")
print("2048> The initial state of the game is: ")
game.printGrid()
print("2048> Please type a command")
try:
    while True:
        text_input = input("--->")
        lexer = Lexer().get_lexer()
        tokens = lexer.lex(text_input)

        try:
            pg = Parser()
            pg.parse()
            parser = pg.get_parser()
            parsed_output = parser.parse(tokens).eval()
            game.play(parsed_output)
            print("2048> Command executed. New state of the grid is: ")
            game.printGrid()
            print_to_stderr(0)
        except ValueError as e:
            print("2048> Error: ",e)
            print_to_stderr(1)
except EOFError as f:
    print("2048> ENCOUNTERED EOF. Exiting!")
    exit()

        