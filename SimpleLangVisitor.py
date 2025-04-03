# Generated from SimpleLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#varDeclaration.
    def visitVarDeclaration(self, ctx:SimpleLangParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#type.
    def visitType(self, ctx:SimpleLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignment.
    def visitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifStatement.
    def visitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#whileStatement.
    def visitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#forStatement.
    def visitForStatement(self, ctx:SimpleLangParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#printStatement.
    def visitPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#inputStatement.
    def visitInputStatement(self, ctx:SimpleLangParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#block.
    def visitBlock(self, ctx:SimpleLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#StringExpr.
    def visitStringExpr(self, ctx:SimpleLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#FloatExpr.
    def visitFloatExpr(self, ctx:SimpleLangParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:SimpleLangParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#IdExpr.
    def visitIdExpr(self, ctx:SimpleLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#AddSub.
    def visitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MultDivMod.
    def visitMultDivMod(self, ctx:SimpleLangParser.MultDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#NotExpr.
    def visitNotExpr(self, ctx:SimpleLangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#IntExpr.
    def visitIntExpr(self, ctx:SimpleLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:SimpleLangParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ParenExpr.
    def visitParenExpr(self, ctx:SimpleLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#LogicalExpr.
    def visitLogicalExpr(self, ctx:SimpleLangParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BooleanExpr.
    def visitBooleanExpr(self, ctx:SimpleLangParser.BooleanExprContext):
        return self.visitChildren(ctx)



del SimpleLangParser