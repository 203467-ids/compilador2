from ast_nodes import *

class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0
    
    def generate(self, ast):
        if isinstance(ast, Program):
            for stmt in ast.children:
                self.generate_statement(stmt)
        return self.code
    
    def generate_statement(self, stmt):
        if isinstance(stmt, VarDeclaration):
            self.generate_var_declaration(stmt)
        elif isinstance(stmt, Assignment):
            self.generate_assignment(stmt)
        elif isinstance(stmt, IfStatement):
            self.generate_if_statement(stmt)
        elif isinstance(stmt, WhileStatement):
            self.generate_while_statement(stmt)
        elif isinstance(stmt, ForStatement):
            self.generate_for_statement(stmt)
        elif isinstance(stmt, PrintStatement):
            self.generate_print_statement(stmt)
        elif isinstance(stmt, InputStatement):
            self.generate_input_statement(stmt)
        elif isinstance(stmt, Block):
            self.generate_block(stmt)
    
    def generate_var_declaration(self, stmt):
        # For variable declarations with initialization
        if stmt.expression:
            result = self.generate_expression(stmt.expression)
            self.emit(f"DECLARE {stmt.var_type} {stmt.name}")
            self.emit(f"ASSIGN {stmt.name} = {result}")
        else:
            # Just declare the variable
            self.emit(f"DECLARE {stmt.var_type} {stmt.name}")
    
    def generate_assignment(self, stmt):
        result = self.generate_expression(stmt.expression)
        self.emit(f"ASSIGN {stmt.name} = {result}")
    
    def generate_if_statement(self, stmt):
        cond_result = self.generate_expression(stmt.condition)
        else_label = self.new_label()
        end_label = self.new_label()
        
        self.emit(f"IF_FALSE {cond_result} GOTO {else_label}")
        
        # Generate then branch
        self.generate_statement(stmt.then_body)
        self.emit(f"GOTO {end_label}")
        
        # Generate else branch if it exists
        self.emit(f"LABEL {else_label}")
        if stmt.else_body:
            self.generate_statement(stmt.else_body)
        
        self.emit(f"LABEL {end_label}")
    
    def generate_while_statement(self, stmt):
        start_label = self.new_label()
        end_label = self.new_label()
        
        self.emit(f"LABEL {start_label}")
        cond_result = self.generate_expression(stmt.condition)
        self.emit(f"IF_FALSE {cond_result} GOTO {end_label}")
        
        # Generate loop body
        self.generate_statement(stmt.body)
        self.emit(f"GOTO {start_label}")
        
        self.emit(f"LABEL {end_label}")
    
    def generate_for_statement(self, stmt):
        start_label = self.new_label()
        cond_label = self.new_label()
        update_label = self.new_label()
        end_label = self.new_label()
        
        # Initialization
        if stmt.init:
            self.generate_statement(stmt.init)
        
        self.emit(f"GOTO {cond_label}")
        
        # Condition checking
        self.emit(f"LABEL {start_label}")
        self.generate_statement(stmt.body)
        
        # Update
        self.emit(f"LABEL {update_label}")
        if stmt.update:
            self.generate_statement(stmt.update)
        
        # Condition
        self.emit(f"LABEL {cond_label}")
        if stmt.condition:
            cond_result = self.generate_expression(stmt.condition)
            self.emit(f"IF_TRUE {cond_result} GOTO {start_label}")
        else:
            # If no condition, loop forever (until break)
            self.emit(f"GOTO {start_label}")
        
        self.emit(f"LABEL {end_label}")
    
    def generate_print_statement(self, stmt):
        result = self.generate_expression(stmt.expression)
        self.emit(f"PRINT {result}")
    
    def generate_input_statement(self, stmt):
        self.emit(f"INPUT {stmt.variable} {stmt.prompt}")
    
    def generate_block(self, stmt):
        for statement in stmt.statements:
            self.generate_statement(statement)
    
    def generate_expression(self, expr):
        if isinstance(expr, BinaryExpr):
            left = self.generate_expression(expr.left)
            right = self.generate_expression(expr.right)
            temp = self.new_temp()
            
            # Map the operator to its intermediate code representation
            op_map = {
                '+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV', '%': 'MOD',
                '<': 'LT', '>': 'GT', '<=': 'LE', '>=': 'GE',
                '==': 'EQ', '!=': 'NE',
                '&&': 'AND', '||': 'OR'
            }
            
            op = op_map.get(expr.operator, expr.operator)
            self.emit(f"{temp} = {left} {op} {right}")
            return temp
        
        elif isinstance(expr, UnaryExpr):
            operand = self.generate_expression(expr.expr)
            temp = self.new_temp()
            
            # Map the operator to its intermediate code representation
            op_map = {'!': 'NOT'}
            
            op = op_map.get(expr.operator, expr.operator)
            self.emit(f"{temp} = {op} {operand}")
            return temp
        
        elif isinstance(expr, VariableExpr):
            # Just return the variable name
            return expr.name
        
        elif isinstance(expr, LiteralExpr):
            # For literals, we might want to create a temporary variable
            # But for simplicity, we'll just return the value
            if expr.value_type == 'string':
                return f'"{expr.value}"'  # Ensure strings are quoted
            return str(expr.value)
    
    def emit(self, code):
        """Add a line of intermediate code."""
        self.code.append(code)
    
    def new_temp(self):
        """Generate a new temporary variable name."""
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp
    
    def new_label(self):
        """Generate a new label for control flow."""
        label = f"L{self.label_count}"
        self.label_count += 1
        return label
