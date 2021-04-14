from rply import ParserGenerator
from ast import MoveSignal, AssignSignal, AssignQuerySignal, VarSignal, QueryValSignal, QueryIDSignal

token_list = ['ADD','SUB','MUL','DIV','LEFT','RIGHT','UP','DOWN','ASSIGN',
            'TO','VAR','IS','VALUE','IN','IDENTIFIER','NUMBER','COMMA','DOT']

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            token_list
            )

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

        @self.pg.production('program : ASSIGN VALUE IN NUMBER COMMA NUMBER TO NUMBER COMMA NUMBER DOT')
        def assignQuery(p):
            x_cord_init = p[3]
            y_cord_init = p[5]
            x_cord = p[7]
            y_cord = p[9]
            return AssignQuerySignal(x_cord_init.value,y_cord_init.value,x_cord.value,y_cord.value)

        @self.pg.production('program : VAR IDENTIFIER IS NUMBER COMMA NUMBER DOT')
        def varName(p):
            tile_name = p[1]
            x_cord = p[3]
            y_cord = p[5]
            if tile_name.value in token_list:
                raise ValueError("Operation not done. Keyword %s cannot be assigned as a variable name" % tile_name.value) 
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

        @self.pg.production('program : VAR ADD IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR SUB IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR MUL IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR DIV IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR LEFT IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR RIGHT IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR UP IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR DOWN IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR ASSIGN IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR TO IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR VAR IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR IS IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR VALUE IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR IN IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR IDENTIFIER IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR NUMBER IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR COMMA IS NUMBER COMMA NUMBER DOT')
        @self.pg.production('program : VAR DOT IS NUMBER COMMA NUMBER DOT')
        def error_varName(p):
            raise  ValueError("The keyword \'%s\' cannot be used as a variable name " %p[1].value)

        @self.pg.error
        def error_handle(token):
            if token.gettokentype() == "$end":
                raise ValueError("The command must end with a \".\"")
            if token.value not in token_list and token.value.upper() in token_list:
                raise ValueError("\"%s\" must be in uppercase" % token.value)
            if token.gettokentype() == "UNIDENTIFIED_TOKEN":
                raise ValueError("SYNTAX ERROR: Please check your syntax around %s" %token.value )
            raise ValueError("Ran into an unexpected %s. Please check your syntax" %token.gettokentype())

    def get_parser(self):
        return self.pg.build()
