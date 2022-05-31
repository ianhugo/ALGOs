


def binary_search(arr, target):

    l, r = 0, len(arr) - 1
    while l + 1 < r:
        mid = 1 + (r - l) // 2 #floor division
        
        if arr[mid] < target:
            l = mid
        else:
            r = mid
    
    if abs(target - arr[l]) <= abs(target - arr[r]):
        return l
    else:
        return r

"""
Tree Properties

1: nodes in a balanced tree
height = x
branch per node = y
nodes = y^x
(for each node, y, for each of those nodes y
so y * y, y * y * y . . .)

2: height of tree in a balance tree
height = log_(branches) nodes


"""
from collections import deque

def bfs(tree):
    visited = [False]*tree.nodes
    prev = [False]*tree.nodes
    queue = deque()
    queue.append(0)
    visited[0] = True

    while not len(queue) == 0:
        node = queue.popleft()
        neighbors = tree[node].neighbors

        for next in neighbors:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                prev[next] = node
    
    return prev

# count number of nodes
# can do some other operations
def dfs(graph, start, n):

    count = 0
    visited = [False] * n
    stack = deque()
    stack.append(start)
    visited[start] = True

    while len(stack) != 0:
        node = stack.pop()
        count += 1
        edges = graph[node].edges

        if edges != []:
            for edge in edges:
                if not visited[edge.to]:
                    stack.append(edge.to)
                    visited[edge.to] = True
    

    return count

"""
Backtracking:
doing a DFS on a deciion tree

decision tree: 
- make a sequence of decisions
- build up partial solutions
- reach full solution

root = "empty" partial solution
leaves = full solution

Knight's Tour
1: Feasibility (find one knight tour)
2: Enumeration (find all knight tour)
3: Counting (how many knight tours)
4: Optimization (knight tour with fewest crossing)

N-Queens

"""