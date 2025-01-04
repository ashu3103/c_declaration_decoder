from objects.basic import *
from objects.array import Array
from objects.function import Function
from objects.identifier import Identifier
from objects.type import Type
from objects.pointer import Pointer
from objects.declarator import Declarator
from constants import *
from utils import *

def dec_parser(tokens, l, r) -> Declarator:
    mid = Declarator(TokenType.DECLARATOR)
    # Create right node -> can be only [x] | (x)
    if (tokens[r][1] == '['):
        right = Array(TokenType.ARRAY, "array", tokens[r+1][1])
    elif (tokens[r][1] == '('):
        right = Function(TokenType.FUNCTION, "function returning", tokens[r+1][1])
    # Create left node -> can be only *, void, char, int, const
    left = None
    l_t = 0
    while(l_t <= l):
        curr = None
        if (tokens[l_t][0] == 'TYPE'):
            curr = Type(TokenType.TYPE, tokens[l_t][1], tokens[l_t][1])
        elif (tokens[l_t][0] == 'POINTER'):
            curr = Pointer(TokenType.POINTER, "pointer to")
        curr.left = left
        left = curr
        l_t = l_t + 1

    mid.left = left
    mid.right = right
    right.left = mid
    left.right = mid
    return mid

def iden_parser(tokens, l, r) -> Identifier:
    mid = Identifier(TokenType.IDENTIFIER, f'{tokens[l+1][1]} is')
    # Create right node -> can be only [x] | (x)
    if (tokens[r][1] == '['):
        right = Array(TokenType.ARRAY, "array", tokens[r+1][1])
    elif (tokens[r][1] == '('):
        right = Function(TokenType.FUNCTION, "function returning", tokens[r+1][1])
    # Create left node -> can be only *, void, char, int, const
    left = None
    l_t = 0
    while(l_t <= l):
        curr = None
        if (tokens[l_t][0] == 'TYPE'):
            curr = Type(TokenType.TYPE, tokens[l_t][1], tokens[l_t][1])
        elif (tokens[l_t][0] == 'POINTER'):
            curr = Pointer(TokenType.POINTER, "pointer to")
        curr.left = left
        left = curr
        l_t = l_t + 1

    mid.left = left
    mid.right = right
    right.left = mid
    left.right = mid
    return mid
