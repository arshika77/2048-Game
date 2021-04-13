from rply import LexerGenerator
from rply import ParserGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('ADD', r'ADD ')
        self.lexer.add('SUB', r'SUBTRACT ')
        self.lexer.add('MUL', r'MULTIPLY ')
        self.lexer.add('DIV', r'DIVIDE ')
        # Parenthesis
        self.lexer.add('LEFT', r'LEFT ')
        self.lexer.add('RIGHT', r'RIGHT ')
        self.lexer.add('UP', r'UP ')
        self.lexer.add('DOWN', r'DOWN ')
        # Semi Colon
        self.lexer.add('ASSIGN', r'ASSIGN ')
        self.lexer.add('TO', r'TO ')
        self.lexer.add('VAR', r'VAR ')
        self.lexer.add('IS', r'IS ')
        # Operators
        self.lexer.add('VALUE', r'VALUE ')
        self.lexer.add('IN', r'IN ')
        #Identifier
        self.lexer.add('IDENTIFIER', r"[a-zA-Z_][a-zA-Z0-9_]*")
        # Number
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('COMMA', r',')
        self.lexer.add('DOT', r'.')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

    
    


