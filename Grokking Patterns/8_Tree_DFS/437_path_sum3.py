"""
Given: root, target
Want: number of paths and paths, where sum of values == target

Strategy:
DFS can find paths

Issue: half paths that sum to target
Could do: carry-over, but just lots of things passed around

Approach:
- pass down variable: curren path
- at each: add node to path
- at each: sum of all subpaths ending at node
- if one path == target, append, increment
- traverse all paths
- at return: remove current node, backtrack
"""


"""
O(n lg n)
lg n = traverse
n = iterate current path

if unbalanced tree: O(n^2)

O(n) space
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def count_paths(root, S):
    return count_paths_recur(root, S, [])

def count_paths_recur(curr, S, curr_path):
    #reached leaf
  if curr is None:
      return 0

  curr_path.append(curr.val)
  path_count, path_sum = 0, 0

  for i in range(len(curr_path)-1, -1, -1):
      path_sum += curr_path[i]
      if path_sum == S:
          path_count += 1

  path_count += count_paths_recur(curr.left, S, curr_path)
  path_count += count_paths_recur(curr.left, S, curr_path)

  del curr_path[-1]

  return path_count


"""MY DRAFT"""

import functools

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  # TODO: Write your code here

  return -1

def get_val(node):
  return node.val

def recur_find(node, curr_path, res, target):

    #CHOICE/check
    #sum subpaths
    #[n1, n2, n3]
    #add n4
    #want all, [n2, n3, n4], [n3, n4], [n4]
    vals = map(get_val, curr_path)
    running_sum = functools.reduce(lambda a, b: a+b, vals)
    running_sum += node.val
    # for count, val in enumerate(curr_path):
    i = 0
    while i < len(curr_path):
        if running_sum == target:
            res.append(curr_path.append(node))
            running_sum -= vals[i]

    #pre process, then pass down
    curr_path.append(node)

    curr_path1, res1 = recur_find(node.left, curr_path, res, target)
    curr_path2, res2 = recur_find(node.right, curr_path, res, target)

    res = res1 + list(set(res2) - set(res1))
    return curr_path, res