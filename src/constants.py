from enum import Enum

POINTER = '*'

class TypeSpecifier(Enum):
    INT = 'int'
    CHAR = 'char'
    VOID = 'void'

class TypeQualifier(Enum):
    CONST = 'const'

class DeclarationType(Enum):
    PREFIX = 1
    DECLARATOR = 2
    POSTFIX = 3