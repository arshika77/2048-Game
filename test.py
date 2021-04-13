from lexer import Lexer
from parsetrans import Parser

text_input = """
ADD LEFT __init__  #.
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)