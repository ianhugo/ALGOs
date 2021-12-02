"""
Given: binary tree
Want: level-by-level traverse in reverse

Strategy:
same as 102
just append to the start, instead of the end
"""

"""
O(n)
O(n)
"""
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = deque()
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node to the current level
      currentLevel.append(currentNode.val)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.appendleft(currentLevel)

  return result