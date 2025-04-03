# Generated from SimpleLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#program.
    def enterProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#program.
    def exitProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#statement.
    def enterStatement(self, ctx:SimpleLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#statement.
    def exitStatement(self, ctx:SimpleLangParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#varDeclaration.
    def enterVarDeclaration(self, ctx:SimpleLangParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#varDeclaration.
    def exitVarDeclaration(self, ctx:SimpleLangParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#type.
    def enterType(self, ctx:SimpleLangParser.TypeContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#type.
    def exitType(self, ctx:SimpleLangParser.TypeContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assignment.
    def enterAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assignment.
    def exitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#whileStatement.
    def enterWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#whileStatement.
    def exitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#forStatement.
    def enterForStatement(self, ctx:SimpleLangParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#forStatement.
    def exitForStatement(self, ctx:SimpleLangParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#printStatement.
    def enterPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#printStatement.
    def exitPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#inputStatement.
    def enterInputStatement(self, ctx:SimpleLangParser.InputStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#inputStatement.
    def exitInputStatement(self, ctx:SimpleLangParser.InputStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#block.
    def enterBlock(self, ctx:SimpleLangParser.BlockContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#block.
    def exitBlock(self, ctx:SimpleLangParser.BlockContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#StringExpr.
    def enterStringExpr(self, ctx:SimpleLangParser.StringExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#StringExpr.
    def exitStringExpr(self, ctx:SimpleLangParser.StringExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#FloatExpr.
    def enterFloatExpr(self, ctx:SimpleLangParser.FloatExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#FloatExpr.
    def exitFloatExpr(self, ctx:SimpleLangParser.FloatExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:SimpleLangParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:SimpleLangParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#IdExpr.
    def enterIdExpr(self, ctx:SimpleLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#IdExpr.
    def exitIdExpr(self, ctx:SimpleLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#AddSub.
    def enterAddSub(self, ctx:SimpleLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#AddSub.
    def exitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MultDivMod.
    def enterMultDivMod(self, ctx:SimpleLangParser.MultDivModContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MultDivMod.
    def exitMultDivMod(self, ctx:SimpleLangParser.MultDivModContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#NotExpr.
    def enterNotExpr(self, ctx:SimpleLangParser.NotExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#NotExpr.
    def exitNotExpr(self, ctx:SimpleLangParser.NotExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#IntExpr.
    def enterIntExpr(self, ctx:SimpleLangParser.IntExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#IntExpr.
    def exitIntExpr(self, ctx:SimpleLangParser.IntExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:SimpleLangParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:SimpleLangParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ParenExpr.
    def enterParenExpr(self, ctx:SimpleLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ParenExpr.
    def exitParenExpr(self, ctx:SimpleLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#LogicalExpr.
    def enterLogicalExpr(self, ctx:SimpleLangParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#LogicalExpr.
    def exitLogicalExpr(self, ctx:SimpleLangParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#BooleanExpr.
    def enterBooleanExpr(self, ctx:SimpleLangParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#BooleanExpr.
    def exitBooleanExpr(self, ctx:SimpleLangParser.BooleanExprContext):
        pass



del SimpleLangParser