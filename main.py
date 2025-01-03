from resources.dtokenizer import tokenize
from resources.utils import *
from resources.constants import *
import os

logs_path = os.path.join(os.path.join(os.getcwd(), 'logs'), 'logs.txt')

ipt = 'char* (*(next())()(()))()'

if __name__ == '__main__':
    with open(logs_path, 'w') as f:
        print(logs_path, file=f)
        tokens = tokenize(ipt)
        print(tokens, file=f)
        match_bracket = matchBrackets(tokens)
        print(match_bracket, file=f)
        match_bracket = matchBrackets(tokens)
        print(match_bracket, file=f)
        match_bracket = matchBrackets(tokens)
        print(match_bracket, file=f)

