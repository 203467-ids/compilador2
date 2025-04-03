class ASTNode:
    def __init__(self, line=0, column=0):
        self.line = line
        self.column = column
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        return child
        
    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "line": self.line,
            "column": self.column,
            "children": [child.to_dict() for child in self.children]
        }


class Program(ASTNode):
    def __init__(self, line=0, column=0):
        super().__init__(line, column)
        
    def to_dict(self):
        result = super().to_dict()
        result["statements"] = [child.to_dict() for child in self.children]
        return result


class VarDeclaration(ASTNode):
    def __init__(self, var_type, name, expression=None, line=0, column=0):
        super().__init__(line, column)
        self.var_type = var_type
        self.name = name
        self.expression = expression
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "var_type": self.var_type,
            "name": self.name,
            "has_init": self.expression is not None
        })
        if self.expression:
            result["expression"] = self.expression.to_dict()
        return result


class Assignment(ASTNode):
    def __init__(self, name, expression, line=0, column=0):
        super().__init__(line, column)
        self.name = name
        self.expression = expression
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "name": self.name,
            "expression": self.expression.to_dict()
        })
        return result


class IfStatement(ASTNode):
    def __init__(self, condition, then_body, else_body=None, line=0, column=0):
        super().__init__(line, column)
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "condition": self.condition.to_dict(),
            "then_body": self.then_body.to_dict(),
            "has_else": self.else_body is not None
        })
        if self.else_body:
            result["else_body"] = self.else_body.to_dict()
        return result


class WhileStatement(ASTNode):
    def __init__(self, condition, body, line=0, column=0):
        super().__init__(line, column)
        self.condition = condition
        self.body = body
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "condition": self.condition.to_dict(),
            "body": self.body.to_dict()
        })
        return result


class ForStatement(ASTNode):
    def __init__(self, init, condition, update, body, line=0, column=0):
        super().__init__(line, column)
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "init": self.init.to_dict() if self.init else None,
            "condition": self.condition.to_dict() if self.condition else None,
            "update": self.update.to_dict() if self.update else None,
            "body": self.body.to_dict()
        })
        return result


class PrintStatement(ASTNode):
    def __init__(self, expression, line=0, column=0):
        super().__init__(line, column)
        self.expression = expression
        
    def to_dict(self):
        result = super().to_dict()
        result["expression"] = self.expression.to_dict()
        return result


class InputStatement(ASTNode):
    def __init__(self, variable, prompt, line=0, column=0):
        super().__init__(line, column)
        self.variable = variable
        self.prompt = prompt
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "variable": self.variable,
            "prompt": self.prompt
        })
        return result


class Block(ASTNode):
    def __init__(self, statements=None, line=0, column=0):
        super().__init__(line, column)
        self.statements = statements or []
        
    def to_dict(self):
        result = super().to_dict()
        result["statements"] = [stmt.to_dict() for stmt in self.statements]
        return result


class BinaryExpr(ASTNode):
    def __init__(self, left, operator, right, line=0, column=0):
        super().__init__(line, column)
        self.left = left
        self.operator = operator
        self.right = right
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "operator": self.operator,
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        })
        return result


class UnaryExpr(ASTNode):
    def __init__(self, operator, expr, line=0, column=0):
        super().__init__(line, column)
        self.operator = operator
        self.expr = expr
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "operator": self.operator,
            "expr": self.expr.to_dict()
        })
        return result


class VariableExpr(ASTNode):
    def __init__(self, name, line=0, column=0):
        super().__init__(line, column)
        self.name = name
        
    def to_dict(self):
        result = super().to_dict()
        result["name"] = self.name
        return result


class LiteralExpr(ASTNode):
    def __init__(self, value, value_type, line=0, column=0):
        super().__init__(line, column)
        self.value = value
        self.value_type = value_type
        
    def to_dict(self):
        result = super().to_dict()
        result.update({
            "value": self.value,
            "value_type": self.value_type
        })
        return result
