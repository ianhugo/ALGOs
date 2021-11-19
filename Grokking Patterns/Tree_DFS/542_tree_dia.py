"""
Given: binary tree
Want: diameter

diameter: number of nodes on longest path between any two leafs
may or may not pass through the root

Strategy:
- DFS
- go deep, find two deepest leaves
- backtrack to common ancestor

"""

"""
MY DRAFT

Errors: need to check if curr node is leaf
(but it would be maxed anyway)

when return need to increment
"""


"""
O(n) traverse each node once
O(n) space
"""
class TreeNode:
    def __init__(self, val, left = None, right = None)
        self.val = val
        self.left = left
        self.right = right

class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0
        self.root = None
        self.branch1 = []
        self.branch2 = []
    
    def find_diameter(self, root):

        return -1
    
    def recur_find(self, curr):

        if curr == None:
            return 0
        
        len1 = self.recur_find(curr.left)
        len2 = self.recur_find(curr.right)


        ## CHECK IF leaf node

        #is this lowest common ancestor?
        #if so: return
        self.treeDiameter = max(self.treeDiameter, (len1+len2+1))

        #what's different about the solution
        #it's the longest one we have

        #if not: combine path
        len = max(len1, len2) 

        return len +1


class TreeDiameter2:

  def __init__(self):
    self.treeDiameter = 0

  def find_diameter(self, root):
    self.calculate_height(root)
    return self.treeDiameter

  def calculate_height(self, currentNode):
    if currentNode is None:
      return 0

    leftTreeHeight = self.calculate_height(currentNode.left)
    rightTreeHeight = self.calculate_height(currentNode.right)

    # if the current node doesn't have a left or right subtree, we can't have
    # a path passing through it, since we need a leaf node on each side
    if leftTreeHeight is not None and rightTreeHeight is not None:

      # diameter at the current node will be equal to the height of left subtree +
      # the height of right sub-trees + '1' for the current node
      diameter = leftTreeHeight + rightTreeHeight + 1

      # update the global tree diameter
      self.treeDiameter = max(self.treeDiameter, diameter)

    # height of the current node will be equal to the maximum of the heights of
    # left or right subtrees plus '1' for the current node
    return max(leftTreeHeight, rightTreeHeight) + 1
