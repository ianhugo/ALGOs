"""
GIVEN: two values L, R
WANT: sum of all nodes, between L and R

Recurse through, if between range, just add
if out of range just stops
"""


def range(root, L, R):
    self.ans = 0
    dfs(root)
    return self.ans
    pass

def dfs(node):
    if node:
        if L <= node.val <= R:
            self.ans += node.val
        if L < node.val:
            dfs(node.left)
        if node.val < R:
            dfs(node.right)
    
