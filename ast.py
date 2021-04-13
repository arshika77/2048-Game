class MoveSignal():
    def __init__(self,action,operator):
        self.action = action
        self.operator = operator

    def eval(self):
        if self.action == "ADD":
            if self.operator == "LEFT":
                return [0]
            elif self.operator == "RIGHT":
                return [1]
            elif self.operator == "UP":
                return [2]
            elif self.operator == "DOWN":
                return [3]
        elif self.action == "SUB":
            if self.operator == "LEFT":
                return [4]
            elif self.operator == "RIGHT":
                return [5]
            elif self.operator == "UP":
                return [6]
            elif self.operator == "DOWN":
                return [7]
        elif self.action == "MUL":
            if self.operator == "LEFT":
                return [8]
            elif self.operator == "RIGHT":
                return [9]
            elif self.operator == "UP":
                return [10]
            elif self.operator == "DOWN":
                return [11]
        elif self.action == "DIV":
            if self.operator == "LEFT":
                return [12]
            elif self.operator == "RIGHT":
                return [13]
            elif self.operator == "UP":
                return [14]
            elif self.operator == "DOWN":
                return [15]

class AssignSignal():
    def __init__(self,tile_num,x_cord,y_cord):
        self.tile_num = tile_num
        self.x_cord = x_cord
        self.y_cord = y_cord

    def eval(self):
        return [16,self.tile_num,self.x_cord,self.y_cord]

class VarSignal():
    def __init__(self,tile_name,x_cord,y_cord):
        self.tile_name = tile_name
        self.x_cord = x_cord
        self.y_cord = y_cord

    def eval(self):
        return [17,self.tile_name,self.x_cord,self.y_cord]

class QueryValSignal():
    def __init__(self,x_cord,y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def eval(self):
        return [18,self.x_cord,self.y_cord]

class QueryIDSignal():
    def __init__(self,expressionVal):
        self.expressionVal = expressionVal

    def eval(self):
        return [19,self.expressionVal.value]
