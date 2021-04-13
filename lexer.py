from rply import LexerGenerator
from rply import ParserGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('ADD', r'\bADD\b')
        self.lexer.add('SUB', r'\bSUBTRACT\b')
        self.lexer.add('MUL', r'\bMULTIPLY\b')
        self.lexer.add('DIV', r'\bDIVIDE\b')
        # Parenthesis
        self.lexer.add('LEFT', r'\bLEFT\b')
        self.lexer.add('RIGHT', r'\bRIGHT\b')
        self.lexer.add('UP', r'\bUP\b')
        self.lexer.add('DOWN', r'\bDOWN\b')
        # Semi Colon
        self.lexer.add('ASSIGN', r'\bASSIGN\b')
        self.lexer.add('TO', r'\bTO\b')
        self.lexer.add('VAR', r'\bVAR\b')
        self.lexer.add('IS', r'\bIS\b')
        # Operators
        self.lexer.add('VALUE', r'\bVALUE\b')
        self.lexer.add('IN', r'\bIN\b')
        #Identifier
        self.lexer.add('IDENTIFIER', r"[a-zA-Z_][a-zA-Z0-9_]*")
        # Number
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('DOT', r'\.')
        self.lexer.add('UNIDENTIFIED_TOKEN',r'.')
        # Ignore whitespaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

    
    


