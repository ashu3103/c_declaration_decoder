from constants import *
from ply import lex

tokens = (
    'TYPE',        # For int, char, etc.
    'IDENTIFIER',  # For variable names
    'POINTER',     # For '*'
    'LPAREN',      # For '('
    'RPAREN',      # For ')'
    'SEMICOLON',   # For ';'
    'LBRACKET',    # For '['
    'RBRACKET',    # For ']'
    'NUMBER',      # For numeric constants
)

# Regular expression rules for tokens
t_POINTER = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_TYPE = r'(int|char|void|const|volatile)'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def tokenize(input: str) -> str:
    lexer = lex.lex()
    lexer.input(input.strip())
    return [(tok.type, tok.value) for tok in lexer]
