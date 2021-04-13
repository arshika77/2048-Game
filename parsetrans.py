from rply import ParserGenerator
from ast import Number, Sum, Sub, Mul, Div

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['ADD','SUB','MUL','DIV','LEFT','RIGHT','UP','DOWN','ASSIGN',
            'TO','VAR','IS','VALUE','IN','IDENTIFIER','NUMBER','COMMA','DOT'])

    def parse(self):
        
        @self.pg.production()
        

        
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
