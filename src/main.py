from dtokenizer import *
from utils import *
from dparser import *
from constants import *
import os
import copy

logs_path = os.path.join(os.path.join(os.getcwd(), 'logs'), 'logs.txt')

ipt = 'char* (*(*foo[5])(char))[]'

if __name__ == '__main__':
    with open(logs_path, 'w') as f:
        print(logs_path, file=f)
        tokens = tokenize(ipt)
        print(tokens, file=f)
        original_tokens = copy.deepcopy(tokens)
        prev_l = 0
        curr = None
        head = None
        while(mb := matchBrackets(original_tokens)):
            curr = dec_parser(tokens, mb[0]-prev_l-1, mb[1]-prev_l+1)
            tokens = tokens[mb[0]-prev_l+1:mb[1]-prev_l]
            prev_l = mb[0]+1
            curr.parent = head
            head = curr
        curr = iden_parser(tokens, getIdentifierIndex(tokens)-1, getIdentifierIndex(tokens)+1)
        curr.parent = head
        head = curr

        ans = ""
        print(ans, file=f)



