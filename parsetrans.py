from rply import ParserGenerator
from ast import MoveSignal, AssignSignal, VarSignal, QueryValSignal, QueryIDSignal

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['ADD','SUB','MUL','DIV','LEFT','RIGHT','UP','DOWN','ASSIGN',
            'TO','VAR','IS','VALUE','IN','IDENTIFIER','NUMBER','COMMA','DOT'])

    def parse(self):
        
        @self.pg.production('program : ADD LEFT DOT')
        @self.pg.production('program : ADD RIGHT DOT')
        @self.pg.production('program : ADD UP DOT')
        @self.pg.production('program : ADD DOWN DOT')
        @self.pg.production('program : SUB LEFT DOT')
        @self.pg.production('program : SUB RIGHT DOT')
        @self.pg.production('program : SUB UP DOT')
        @self.pg.production('program : SUB DOWN DOT')
        @self.pg.production('program : MUL LEFT DOT')
        @self.pg.production('program : MUL RIGHT DOT')
        @self.pg.production('program : MUL UP DOT')
        @self.pg.production('program : MUL DOWN DOT')
        @self.pg.production('program : DIV LEFT DOT')
        @self.pg.production('program : DIV RIGHT DOT')
        @self.pg.production('program : DIV UP DOT')
        @self.pg.production('program : DIV DOWN DOT')
        def program(p):
            action = p[0]
            operator = p[1]
            return MoveSignal(action.value,operator.value)

        @self.pg.production('program : ASSIGN NUMBER TO NUMBER COMMA NUMBER DOT')
        def assign(p):
            tile_num = p[1]
            x_cord = p[3]
            y_cord = p[5]
            return AssignSignal(tile_num.value,x_cord.value,y_cord.value)

        @self.pg.production('program : VAR IDENTIFIER IS NUMBER COMMA NUMBER DOT')
        def varName(p):
            tile_name = p[1]
            x_cord = p[3]
            y_cord = p[5]
            return VarSignal(tile_name.value,x_cord.value,y_cord.value)

        @self.pg.production('program : VALUE IN NUMBER COMMA NUMBER DOT')
        def queryFuncOne(p):
            x_cord = p[2]
            y_cord = p[4]
            return QueryValSignal(x_cord.value,y_cord.value)

        @self.pg.production('program : VALUE IN IDENTIFIER DOT')
        def queryFuncTwo(p):
            expressionVal = p[2]
            return QueryIDSignal(expressionVal)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
