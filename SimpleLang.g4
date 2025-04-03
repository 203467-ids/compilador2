grammar SimpleLang;

// Parser rules
program
    : statement+ EOF
    ;

statement
    : varDeclaration ';'
    | assignment ';'
    | ifStatement
    | whileStatement
    | forStatement
    | printStatement ';'
    | inputStatement ';'
    | block
    ;

varDeclaration
    : type ID ('=' expression)?
    ;

type
    : 'int'
    | 'float'
    | 'string'
    | 'boolean'
    ;

assignment
    : ID '=' expression
    ;

ifStatement
    : 'if' '(' expression ')' statement ('else' statement)?
    ;

whileStatement
    : 'while' '(' expression ')' statement
    ;

forStatement
    : 'for' '(' (varDeclaration | assignment)? ';' expression? ';' assignment? ')' statement
    ;

printStatement
    : 'print' '(' expression ')'
    ;

inputStatement
    : ID '=' 'input' '(' STRING ')'
    ;

block
    : '{' statement* '}'
    ;

expression
    : expression ('*' | '/' | '%') expression  # MultDivMod
    | expression ('+' | '-') expression        # AddSub
    | expression ('<' | '>' | '<=' | '>=') expression # RelationalExpr
    | expression ('==' | '!=') expression     # EqualityExpr
    | expression ('&&' | '||') expression     # LogicalExpr
    | '!' expression                          # NotExpr
    | '(' expression ')'                      # ParenExpr
    | ID                                      # IdExpr
    | INT                                     # IntExpr
    | FLOAT                                   # FloatExpr
    | STRING                                  # StringExpr
    | BOOLEAN                                 # BooleanExpr
    ;

// Lexer rules
ID      : [a-zA-Z][a-zA-Z0-9_]* ;
INT     : [0-9]+ ;
FLOAT   : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING  : '"' (~["\r\n] | '\\"')* '"' ;
BOOLEAN : 'true' | 'false' ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
