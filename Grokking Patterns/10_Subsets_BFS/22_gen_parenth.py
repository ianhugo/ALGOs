"""
Given: n pairs of parentheses
Want: gen all combinations of balanced parentheses

Recursion: each step
- inside each
- or next to each
- unwind when hit base case
- when recurse back, is the same, only keep one

1: can't add more than n open parentheses (
2: add ) when have enough open
Approach: add ) or ( to the end
- add ) if 

"""

"""
time complexity = catalan number
O(n * 2^n) space
"""

from collections import deque

class parent:
    def __init__(self, str1, open, close):
        self.str1 = str1
        self.open = open
        self.close = close

def gen(num):
    res = []
    queue = deque()
    queue.append(parent("", 0, 0))

    while queue:
        ps = queue.popleft()    #queue it each time

        if ps.open == num and ps.close == num:  #final
            res.append(ps.str1)
        
        else:
            if ps.open < num: #if can add open
                queue.append(parent(ps.str1 + "(", ps.open +1, ps.close))
            
            if ps.open > ps.close:  #if can add close
                queue.append(parent(ps.str1 + ")", ps.open, ps.count +1))
    
    return res