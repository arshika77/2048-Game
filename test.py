from lexer import Lexer
from parsetrans import Parser

text_input = """
    VAR XYZ IS 2,3.
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
print(parser.parse(tokens).eval())