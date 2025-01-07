from dtokenizer import *
from constants import *
from graph import *
import os

logs_path = os.path.join(os.path.join(os.getcwd(), 'logs'), 'logs.txt')

ipt = 'char* foo(char*)'

if __name__ == '__main__':
    with open(logs_path, 'w') as f:
        tokens = tokenize(ipt)
        head: Identifier | Declarator = generateGraph(tokens)
        ans = traverseGraph(head)
        print(ans, file=f)



