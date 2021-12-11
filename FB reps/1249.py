"""
Drafts solutions
GIVEN: string
WANT: valid parentheses, remove some

"""

def solve(st):
    indices = set()
    stack = []

    for i, c in enumerate(st):
        if c not in "()":
            continue
        if c == "(":    #match open, all added
            stack.append(i)
        elif not stack: #if empty but closedd, then add
            indices.add(i)
        else:       #match close, pop however many closed
            stack.pop()
    
    indices = indices.union(set(stack)) #all invalids

    string = []

    for i,c in enumerate(st):
        if i not in indices:
            string.append(c)
    
    return "".join(string)