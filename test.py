from lexer import Lexer
from parsetrans import Parser

text_input = """
    ASSIGN VALUE IN 2,3 TO 4,5.
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
print(parser.parse(tokens).eval())