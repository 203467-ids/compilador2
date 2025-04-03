from antlr4 import *
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from symbol_table import SymbolTable, Symbol
from ast_nodes import *

class SemanticAnalyzer(SimpleLangVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext, ast=None):
        if ast:
            for child in ast.children:
                self.analyze_node(child)
        return self.symbol_table.to_dict(), self.errors
    
    def analyze_node(self, node):
        if isinstance(node, VarDeclaration):
            self.analyze_var_declaration(node)
        elif isinstance(node, Assignment):
            self.analyze_assignment(node)
        elif isinstance(node, IfStatement):
            self.analyze_if_statement(node)
        elif isinstance(node, WhileStatement):
            self.analyze_while_statement(node)
        elif isinstance(node, ForStatement):
            self.analyze_for_statement(node)
        elif isinstance(node, PrintStatement):
            self.analyze_print_statement(node)
        elif isinstance(node, InputStatement):
            self.analyze_input_statement(node)
        elif isinstance(node, Block):
            self.analyze_block(node)
        
    def analyze_var_declaration(self, node):
        # Add the variable to the symbol table
        if node.expression:
            expr_type = self.get_expression_type(node.expression)
            if expr_type and not self.are_types_compatible(node.var_type, expr_type):
                self.errors.append(f"Error semántico - Línea {node.line}:{node.column}: No se puede asignar valor de tipo '{expr_type}' a variable de tipo '{node.var_type}'")
        
        self.symbol_table.define(node.name, node.var_type, None, node.line, node.column)
    
    def analyze_assignment(self, node):
        # Check if the variable exists
        symbol = self.symbol_table.resolve(node.name, node.line, node.column)
        if symbol:
            # Check if the types are compatible
            expr_type = self.get_expression_type(node.expression)
            if expr_type and not self.are_types_compatible(symbol.type_name, expr_type):
                self.errors.append(f"Error semántico - Línea {node.line}:{node.column}: No se puede asignar valor de tipo '{expr_type}' a variable de tipo '{symbol.type_name}'")
            # Mark the variable as initialized
        symbol.initialized = True
    
    def analyze_if_statement(self, node):
        # Check condition type
        cond_type = self.get_expression_type(node.condition)
        if cond_type and cond_type != 'boolean':
            self.errors.append(f"Error semántico - Línea {node.line}:{node.column}: Condición del if debe ser de tipo boolean, pero se encontró '{cond_type}'")
        
        # Enter new scope for then branch
        self.symbol_table.enter_scope()
        self.analyze_node(node.then_body)
        self.symbol_table.exit_scope()
        
        # Enter new scope for else branch if exists
        if node.else_body:
            self.symbol_table.enter_scope()
            self.analyze_node(node.else_body)
            self.symbol_table.exit_scope()
    
    def analyze_while_statement(self, node):
        # Check condition type
        cond_type = self.get_expression_type(node.condition)
        if cond_type and cond_type != 'boolean':
            self.errors.append(f"Error semántico - Línea {node.line}:{node.column}: Condición del while debe ser de tipo boolean, pero se encontró '{cond_type}'")
        
        # Enter new scope for loop body
        self.symbol_table.enter_scope()
        self.analyze_node(node.body)
        self.symbol_table.exit_scope()
    
    def analyze_for_statement(self, node):
        # Enter new scope for the for loop
        self.symbol_table.enter_scope()
        
        # Analyze init statement if exists
        if node.init:
            self.analyze_node(node.init)
        
        # Check condition type
        if node.condition:
            cond_type = self.get_expression_type(node.condition)
            if cond_type and cond_type != 'boolean':
                self.errors.append(f"Error semántico - Línea {node.line}:{node.column}: Condición del for debe ser de tipo boolean, pero se encontró '{cond_type}'")
        
        # Analyze update statement if exists
        if node.update:
            self.analyze_node(node.update)
        
        # Analyze body
        self.analyze_node(node.body)
        
        # Exit for loop scope
        self.symbol_table.exit_scope()
    
    def analyze_print_statement(self, node):
        # Just check the expression type for validity
        self.get_expression_type(node.expression)
    
    def analyze_input_statement(self, node):
        # Check if the variable exists
        symbol = self.symbol_table.resolve(node.variable, node.line, node.column)
        if symbol:
            # Mark the variable as initialized
            symbol.initialized = True
    
    def analyze_block(self, node):
        # Enter new scope for block
        self.symbol_table.enter_scope()
        
        # Analyze each statement
        for stmt in node.statements:
            self.analyze_node(stmt)
        
        # Exit block scope
        self.symbol_table.exit_scope()
    
    def get_expression_type(self, expr):
        if isinstance(expr, BinaryExpr):
            left_type = self.get_expression_type(expr.left)
            right_type = self.get_expression_type(expr.right)
            
            # Arithmetic operators: +, -, *, /, %
            if expr.operator in ['+', '-', '*', '/', '%']:
                if left_type in ['int', 'float'] and right_type in ['int', 'float']:
                    return 'float' if 'float' in [left_type, right_type] else 'int'
                elif expr.operator == '+' and ('string' in [left_type, right_type]):
                    # String concatenation
                    return 'string'
                else:
                    self.errors.append(f"Error semántico - Línea {expr.line}:{expr.column}: Tipos incompatibles para operador '{expr.operator}': '{left_type}' y '{right_type}'")
                    return None
            
            # Relational operators: <, >, <=, >=
            elif expr.operator in ['<', '>', '<=', '>=']:
                if left_type in ['int', 'float'] and right_type in ['int', 'float']:
                    return 'boolean'
                else:
                    self.errors.append(f"Error semántico - Línea {expr.line}:{expr.column}: Tipos incompatibles para operador '{expr.operator}': '{left_type}' y '{right_type}'")
                    return None
            
            # Equality operators: ==, !=
            elif expr.operator in ['==', '!=']:
                if left_type == right_type or (left_type in ['int', 'float'] and right_type in ['int', 'float']):
                    return 'boolean'
                else:
                    self.errors.append(f"Error semántico - Línea {expr.line}:{expr.column}: Tipos incompatibles para operador '{expr.operator}': '{left_type}' y '{right_type}'")
                    return None
            
            # Logical operators: &&, ||
            elif expr.operator in ['&&', '||']:
                if left_type == 'boolean' and right_type == 'boolean':
                    return 'boolean'
                else:
                    self.errors.append(f"Error semántico - Línea {expr.line}:{expr.column}: Tipos incompatibles para operador '{expr.operator}': '{left_type}' y '{right_type}'")
                    return None
            
        elif isinstance(expr, UnaryExpr):
            operand_type = self.get_expression_type(expr.expr)
            
            # Logical NOT: !
            if expr.operator == '!' and operand_type == 'boolean':
                return 'boolean'
            else:
                self.errors.append(f"Error semántico - Línea {expr.line}:{expr.column}: Tipo incompatible para operador '{expr.operator}': '{operand_type}'")
                return None
        
        elif isinstance(expr, VariableExpr):
            # Look up the variable in the symbol table
            symbol = self.symbol_table.resolve(expr.name, expr.line, expr.column)
            if symbol:
                if not symbol.initialized:
                    self.errors.append(f"Error semántico - Línea {expr.line}:{expr.column}: Variable '{expr.name}' utilizada sin inicializar.")
                return symbol.type_name
            return None
        
        elif isinstance(expr, LiteralExpr):
            return expr.value_type
        
        return None
    
    def are_types_compatible(self, target_type, source_type):
        if target_type == source_type:
            return True
        
        # Allow int to float conversion
        if target_type == 'float' and source_type == 'int':
            return True
        
        return False
