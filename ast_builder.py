from antlr4 import *
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from ast_nodes import *

class ASTBuilder(SimpleLangVisitor):
    def __init__(self):
        self.errors = []
        
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        program = Program(ctx.start.line, ctx.start.column)
        for stmt_ctx in ctx.statement():
            stmt = self.visit(stmt_ctx)
            if stmt:
                program.add_child(stmt)
        return program
    
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        if ctx.varDeclaration():
            return self.visit(ctx.varDeclaration())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.printStatement():
            return self.visit(ctx.printStatement())
        elif ctx.inputStatement():
            return self.visit(ctx.inputStatement())
        elif ctx.block():
            return self.visit(ctx.block())
    
    def visitVarDeclaration(self, ctx:SimpleLangParser.VarDeclarationContext):
        var_type = ctx.type_().getText()
        var_name = ctx.ID().getText()
        expression = None
        if ctx.expression():
            expression = self.visit(ctx.expression())
        return VarDeclaration(var_type, var_name, expression, ctx.start.line, ctx.start.column)
    
    def visitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        expression = self.visit(ctx.expression())
        return Assignment(var_name, expression, ctx.start.line, ctx.start.column)
    
    def visitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.statement(0))
        else_stmt = None
        if len(ctx.statement()) > 1:
            else_stmt = self.visit(ctx.statement(1))
        return IfStatement(condition, then_stmt, else_stmt, ctx.start.line, ctx.start.column)
    
    def visitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        condition = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        return WhileStatement(condition, body, ctx.start.line, ctx.start.column)
    
    def visitForStatement(self, ctx:SimpleLangParser.ForStatementContext):
        init = None
        if ctx.varDeclaration():
            init = self.visit(ctx.varDeclaration())
        elif ctx.assignment(0):
            init = self.visit(ctx.assignment(0))
            
        condition = None
        if ctx.expression():
            condition = self.visit(ctx.expression())
            
        update = None
        if len(ctx.assignment()) > 0:
            if ctx.varDeclaration() and ctx.assignment(0):
                update = self.visit(ctx.assignment(0))
            elif len(ctx.assignment()) > 1:
                update = self.visit(ctx.assignment(1))
                
        body = self.visit(ctx.statement())
        return ForStatement(init, condition, update, body, ctx.start.line, ctx.start.column)
    
    def visitPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        expression = self.visit(ctx.expression())
        return PrintStatement(expression, ctx.start.line, ctx.start.column)
    
    def visitInputStatement(self, ctx:SimpleLangParser.InputStatementContext):
        var_name = ctx.ID().getText()
        prompt = ctx.STRING().getText()
        return InputStatement(var_name, prompt, ctx.start.line, ctx.start.column)
    
    def visitBlock(self, ctx:SimpleLangParser.BlockContext):
        block = Block([], ctx.start.line, ctx.start.column)
        for stmt_ctx in ctx.statement():
            stmt = self.visit(stmt_ctx)
            if stmt:
                block.statements.append(stmt)
        return block
    
    def visitMultDivMod(self, ctx:SimpleLangParser.MultDivModContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpr(left, op, right, ctx.start.line, ctx.start.column)
    
    def visitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpr(left, op, right, ctx.start.line, ctx.start.column)
    
    def visitRelationalExpr(self, ctx:SimpleLangParser.RelationalExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpr(left, op, right, ctx.start.line, ctx.start.column)
    
    def visitEqualityExpr(self, ctx:SimpleLangParser.EqualityExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpr(left, op, right, ctx.start.line, ctx.start.column)
    
    def visitLogicalExpr(self, ctx:SimpleLangParser.LogicalExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpr(left, op, right, ctx.start.line, ctx.start.column)
    
    def visitNotExpr(self, ctx:SimpleLangParser.NotExprContext):
        expr = self.visit(ctx.expression())
        return UnaryExpr('!', expr, ctx.start.line, ctx.start.column)
    
    def visitParenExpr(self, ctx:SimpleLangParser.ParenExprContext):
        return self.visit(ctx.expression())
    
    def visitIdExpr(self, ctx:SimpleLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        return VariableExpr(var_name, ctx.start.line, ctx.start.column)
    
    def visitIntExpr(self, ctx:SimpleLangParser.IntExprContext):
        value = int(ctx.INT().getText())
        return LiteralExpr(value, 'int', ctx.start.line, ctx.start.column)
    
    def visitFloatExpr(self, ctx:SimpleLangParser.FloatExprContext):
        value = float(ctx.FLOAT().getText())
        return LiteralExpr(value, 'float', ctx.start.line, ctx.start.column)
    
    def visitStringExpr(self, ctx:SimpleLangParser.StringExprContext):
        value = ctx.STRING().getText()
        # Remove the surrounding quotes
        value = value[1:-1]
        return LiteralExpr(value, 'string', ctx.start.line, ctx.start.column)
    
    def visitBooleanExpr(self, ctx:SimpleLangParser.BooleanExprContext):
        value = ctx.BOOLEAN().getText() == 'true'
        return LiteralExpr(value, 'boolean', ctx.start.line, ctx.start.column)
