"""
Given: int[n] each of height value
ocean = right of the builds
ocean view for building i, building[i+1] lower height

WANT: buildings with ocean view, sorted increasing


Enter:
array of ints
[1, 3, 5, 2, 4, 7]

OCEAN = RHS of all

IDEA 1: 
- go from right to left
- have a running max
- if larger than running max = get view
- update running max
- reversed  = increasing order

LEARNED:
- use stack to track candidates
- pop stack, when xx
- append stack, when yy
- stack full = zz
- stack empty = qq

MONOTONIC STACK:
- elements, keep increasing order
Previous Less element
- find the element, previously less than current
Next Less element
- find element, next that is less than current
"""

def views(h):
    n = len(h)
    res = []

    stack = []

    for curr in range(n, 0, -1):
        
        #if latest on stack height, shorter than curr height
        while stack and h[stack[-1]] < h[curr]: 
            stack.pop() #if taller than everyone, will pop everyone
                        #then it will be empty stack condition

        if not stack:   #no buildings to the right, taller
            res.append(curr)
        
        stack.append(curr)
    
    res.reverse()

    return res