
"""
Does BT have this sequence of numbers as root to leaf
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, seq):
    if not root:
        return len(seq) == 0
    
    return find_path_recursive(root, seq, 0)

def find_path_recursive(curr, seq, seqidx):

    #base case
    if curr is None:
        return False
    
    seqLen = len(seq)

    #exceed
    #stopping early
    if seqidx >= seqLen or curr.val != seq[seqidx]:
        return False
    
    if curr.left is None and curr.right is None and seqidx == seqLen -1:
        return True
    
    return find_path_recursive(curr.left, seq, seqidx+1) or find_path_recursive(curr.right, seq, seqidx+1)