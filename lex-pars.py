from rply import LexerGenerator
from rply import ParserGenerator

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

    
    


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['add', 'subtract', 'multiply', 'divide', 'left', 'right', 'up', 'down', 'assign', 'to', 'var', 'is', 'value', 'in', 'number', 'dot', 'comma'])

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : NUMBER')
        
        def program(p):
            return Print(p[2])

        
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
