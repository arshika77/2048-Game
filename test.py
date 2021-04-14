from lexer import Lexer
from parsetrans import Parser
from gameFunctions import Grid2048

game = Grid2048(4)
game.addNumber('normal')

print("2048> Welcome to the 2048-game engine @DevelopedBy Arshika ")
print("2048> The initial state of the game is: ")
game.printGrid()
print("2048> Please type a command")

while True:
    text_input = input("--->")
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    try:
        pg = Parser()
        pg.parse()
        parser = pg.get_parser()
        parsed_output = parser.parse(tokens).eval()
        print("2048> Output parsed")
        print("2048> ",parsed_output)
        game.play(parsed_output)
        print("Command executed. New state of the grid is: ")
        game.printGrid()
    except ValueError as e:
        print("2048> Error: ",e)

        