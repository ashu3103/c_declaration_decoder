from utils import *
from dparser import *
import copy

def generateGraph(original_tokens):
    tokens = copy.deepcopy(original_tokens)
    prev_l = 0
    curr = None
    head = None
    while(mb := matchBrackets(original_tokens)):
        curr = decParser(tokens, mb[0]-prev_l-1, mb[1]-prev_l+1)
        tokens = tokens[mb[0]-prev_l+1:mb[1]-prev_l]
        prev_l = mb[0]+1
        curr.parent = head
        head = curr
    curr = idenParser(tokens, getIdentifierIndex(tokens)-1, getIdentifierIndex(tokens)+1)
    curr.parent = head
    head = curr
    return head

def traverseRight(head: Identifier | Declarator) -> str:
    curr = head
    ans = ""
    while(curr):
        if curr.message:
            ans = concatString(ans, curr.printMessage())
        curr = curr.right
    return ans

def traverseLeft(head: Identifier | Declarator) -> str:
    curr = head
    ans = ""
    while(curr):
        if curr.message:
            ans = concatString(ans, curr.printMessage())
        curr = curr.left
    return ans

def traverseGraph(head: Identifier | Declarator) -> str:
    ans = ""
    curr = head
    while(curr):
        if (curr.message):
            ans = concatString(ans, curr.printMessage())
        # traverse right
        ans = concatString(ans, traverseRight(curr.right))
        # traverse left
        ans = concatString(ans, traverseLeft(curr.left))
        curr = curr.parent
    return ans