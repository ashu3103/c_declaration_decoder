from enum import Enum

class TokenType(Enum):
    TYPE = 0,
    IDENTIFIER = 1,
    POINTER = 2,
    ARRAY = 3,
    FUNCTION = 4,
    SEMICOLON = 5,
    DECLARATOR = 6

class TypeSpecifier(Enum):
    INT = 'int'
    CHAR = 'char'
    VOID = 'void'

class TypeQualifier(Enum):
    CONST = 'const'