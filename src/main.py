from dtokenizer import *
from utils import *
from dparser import *
from constants import *
import os

logs_path = os.path.join(os.path.join(os.getcwd(), 'logs'), 'logs.txt')

ipt = 'char* const next[4]'

if __name__ == '__main__':
    with open(logs_path, 'w') as f:
        print(logs_path, file=f)
        tokens = tokenize(ipt)
        print(tokens, file=f)
        
        while(mb := matchBrackets(tokens)):
            print(mb, file=f)
        head = iden_parser(tokens, getIdentifierIndex(tokens)-1, getIdentifierIndex(tokens)+1)

        # show result
        ans = ""
        curr = head
        ans = ans + curr.printMessage()
          ## Jump to right
        if (curr := curr.right):
            ans = ans + " " + curr.printMessage()
            curr = head
        while (curr := curr.left):
            ans = ans + " " + curr.printMessage()
        
        print(ans, file=f)



