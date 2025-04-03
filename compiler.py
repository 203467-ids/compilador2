import sys
import os
import json
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from ast_builder import ASTBuilder
from semantic_analyzer import SemanticAnalyzer
from intermediate_code_gen import IntermediateCodeGenerator

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.lexer_errors = []
        self.syntax_errors = []
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_type = "léxico" if isinstance(recognizer, SimpleLangLexer) else "sintáctico"
        error = f"Error {error_type} - Línea {line}:{column}: {msg}"
        
        if isinstance(recognizer, SimpleLangLexer):
            self.lexer_errors.append(error)
        else:
            self.syntax_errors.append(error)

class Compiler:
    def __init__(self):
        self.lexer_errors = []
        self.syntax_errors = []
        self.semantic_errors = []
        self.ast = None
        self.symbol_table = None
        self.intermediate_code = []
        
    def compile(self, input_text):
        # Crear el input stream
        input_stream = InputStream(input_text)
        
        # Crear un error listener personalizado
        error_listener = CustomErrorListener()
        
        # Análisis léxico
        lexer = SimpleLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)
        token_stream = CommonTokenStream(lexer)
        
        # Análisis sintáctico
        parser = SimpleLangParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        parse_tree = parser.program()
        
        # Recopilar errores léxicos y sintácticos
        self.lexer_errors = error_listener.lexer_errors
        self.syntax_errors = error_listener.syntax_errors
        
        # Si hay errores léxicos o sintácticos, terminamos
        if self.lexer_errors or self.syntax_errors:
            return self.get_compilation_result()
        
        # Construcción del AST
        ast_builder = ASTBuilder()
        self.ast = ast_builder.visit(parse_tree)
        
        # Análisis semántico
        semantic_analyzer = SemanticAnalyzer()
        self.symbol_table, semantic_errors = semantic_analyzer.visitProgram(None, self.ast)
        self.semantic_errors = semantic_errors
        
        # Si hay errores semánticos, terminamos
        if self.semantic_errors:
            return self.get_compilation_result()
        
        # Generación de código intermedio
        code_generator = IntermediateCodeGenerator()
        self.intermediate_code = code_generator.generate(self.ast)
        
        return self.get_compilation_result()
    
    def get_compilation_result(self):
        return {
            "success": not (self.lexer_errors or self.syntax_errors or self.semantic_errors),
            "lexer_errors": self.lexer_errors,
            "syntax_errors": self.syntax_errors,
            "semantic_errors": self.semantic_errors,
            "ast": self.ast.to_dict() if self.ast else None,
            "symbol_table": self.symbol_table,
            "intermediate_code": self.intermediate_code
        }

# Para pruebas desde línea de comandos
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Leer el archivo de código fuente
        with open(sys.argv[1], 'r') as file:
            source_code = file.read()
        
        compiler = Compiler()
        result = compiler.compile(source_code)
        
        # Imprimir el resultado en formato JSON
        print(json.dumps(result, indent=2))
    else:
        print("Uso: python compiler.py <archivo_fuente>")
