from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('add', r'ADD')
        self.lexer.add('subtract', r'SUBTRACT')
        self.lexer.add('multiply', r'MULTIPLY')
        self.lexer.add('divide', r'DIVIDE')
        # Parenthesis
        self.lexer.add('left', r'LEFT')
        self.lexer.add('right', r'RIGHT')
        self.lexer.add('up', r'UP')
        self.lexer.add('down', r'DOWN')
        # Semi Colon
        self.lexer.add('assign', r'ASSIGN')
        self.lexer.add('to', r'TO')
        self.lexer.add('var', r'VAR')
        self.lexer.add('is', r'IS')
        # Operators
        self.lexer.add('value', r'VALUE')
        self.lexer.add('in', r'IN')
        # Number
        self.lexer.add('number', r'\d+')
        self.lexer.add('dot', r'.')
        self.lexer.add('comma', r',')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
