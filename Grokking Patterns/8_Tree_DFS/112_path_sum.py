"""
Find if tree has a path that sums to target

DFS recursion

O(n)
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  if root is None:
    return False

  # if the current node is a leaf and its value is equal to the sum, we've found a path
  if root.val == sum and root.left is None and root.right is None:
    return True

  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true
  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)

