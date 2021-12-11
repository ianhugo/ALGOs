"""
Given: absolute path
WANT: canonical path

IDEA:
- given a bunch of UNIX commands for directory
- when given "..", means went up a directory
- thus pop that directory

"""



def simplify(path):
    
    stack = []

    for portion in path.split("/"):

        if portion == "..": #go up one level
            if stack:
                stack.pop()
        
        elif portion == "." or not portion: #not an op
            continue

        else:   #valid directory
            stack.append(portion)
    
    final_str = "/" + "/".join(stack)

    return final_str