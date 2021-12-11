"""
Vertical order traversal of BT

O(nlg n)
"""

from collections import deque

def solve(root):
    columns = {}
    queue = deque([root, 0])

    while queue:
        node, column = queue.popleft()

        if node is not None:
            columns[column].append(node.val) #top to bottom order

            queue.append((node.left, column-1)) #use this to keep track of columns
            queue.append((node.right, column+1))
    
    return [columns[x] for x in sorted(columns.keys())] #L to R order


"""no sorting

if keep track of the range of columns
then no need to sort

O(n)

"""

def solve2(root):

    if root is None:
        return []

    cols = {}

    min_c = max_c = 0

    q = deque([root, 0])

    while q:

        node, col = q.popleft()

        if node is not None:
            cols[col].append(node.val)

            min_c = min(min_c, col)
            max_c = max(max_c, col)

            q.append([node.left, col-1])
            q.append([node.right, col+1])
    
    return [cols[x] for x in range(min_c, max_c +1)]