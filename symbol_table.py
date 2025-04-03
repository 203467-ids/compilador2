class Symbol:
    def __init__(self, name, type_name, value=None, line=0, column=0):
        self.name = name
        self.type_name = type_name
        self.value = value
        self.line = line
        self.column = column
        self.initialized = value is not None

    def __str__(self):
        return f"Symbol(name={self.name}, type={self.type_name}, value={self.value}, initialized={self.initialized})"


class Scope:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
        self.children = []

    def define(self, symbol):
        self.symbols[symbol.name] = symbol
        return symbol

    def resolve(self, name):
        if name in self.symbols:
            return self.symbols[name]
        
        if self.parent:
            return self.parent.resolve(name)
        
        return None

    def add_child(self, scope):
        self.children.append(scope)
        return scope


class SymbolTable:
    def __init__(self):
        self.global_scope = Scope()
        self.current_scope = self.global_scope
        self.errors = []

    def enter_scope(self):
        new_scope = Scope(self.current_scope)
        self.current_scope.add_child(new_scope)
        self.current_scope = new_scope
        return new_scope

    def exit_scope(self):
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent
        return self.current_scope

    def define(self, name, type_name, value=None, line=0, column=0):
        # Check if symbol is already defined in the current scope
        if name in self.current_scope.symbols:
            self.errors.append(f"Error semántico - Línea {line}:{column}: Variable '{name}' ya ha sido declarada en este ámbito.")
            return None
        
        symbol = Symbol(name, type_name, value, line, column)
        return self.current_scope.define(symbol)

    def resolve(self, name, line=0, column=0):
        symbol = self.current_scope.resolve(name)
        if symbol is None:
            self.errors.append(f"Error semántico - Línea {line}:{column}: Variable '{name}' no ha sido declarada.")
        return symbol

    def get_all_symbols(self):
        """Get all symbols in the symbol table as a flat list."""
        result = []
        
        def collect_symbols(scope):
            for symbol in scope.symbols.values():
                result.append(symbol)
            for child in scope.children:
                collect_symbols(child)
        
        collect_symbols(self.global_scope)
        return result

    def to_dict(self):
        """Convert symbol table to a dictionary for easy JSON serialization."""
        symbols = self.get_all_symbols()
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type_name,
                    "value": s.value,
                    "initialized": s.initialized,
                    "line": s.line,
                    "column": s.column
                }
                for s in symbols
            ],
            "errors": self.errors
        }
