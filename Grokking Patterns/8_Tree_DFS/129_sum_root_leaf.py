"""
Given: binary tree with unit digits
Want: sum of digits on paths

O(n) time
O(n) space
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_sum_numbers(root):
    return find_root_leaf_numbers(root, 0)



def find_root_leaf_numbers(curr, pathSum):
    
    #hit sentry
    if curr is None:
        return 0

    #calculate path number of curr node
    #update pathSUm
    pathSum = 10 * pathSum + curr.val

    #if leaf
    if curr.left is None and curr.right is None:
        return pathSum
    
    #pass down pathsum
    #once hit leaf, will unwind recursion
    #return true pathSUm all the way
    #want to do add as on the callback, can add up all
    return find_root_leaf_numbers(curr.left, pathSum) +\
        find_root_leaf_numbers(curr.right, pathSum)

#have base cases
#when to return
#do preprocessing, then pass down
#do post processing, then pass up