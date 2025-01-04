def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

def getIdentifierIndex(tokens):
    for i in range(len(tokens)):
        if tokens[i][0] == 'IDENTIFIER':
            return i
    
    raise Exception('tokens doesn\'t contain an identifier')

@static_vars(next = None, match_bracket = {})
def matchBrackets(tokens):
    identifier_index = getIdentifierIndex(tokens)
    
    if matchBrackets.next == None:
        stack = []
        for i in range(len(tokens)):
            if (tokens[i][1] == '('):
                stack.append(i)
            elif (tokens[i][1] == ')'):
                match = stack.pop()
                if identifier_index < i and identifier_index > match:
                    matchBrackets.match_bracket[match] = i
        
        ## Sort by key
        matchBrackets.match_bracket = {key: matchBrackets.match_bracket[key] for key in sorted(matchBrackets.match_bracket)}
        if (len(matchBrackets.match_bracket)):
            matchBrackets.next = 0
            return list(matchBrackets.match_bracket.items())[matchBrackets.next]
        
        return None

    elif matchBrackets.next == len(matchBrackets.match_bracket)-1:
        return None
    else:
        matchBrackets.next = matchBrackets.next + 1
        return list(matchBrackets.match_bracket.items())[matchBrackets.next]
