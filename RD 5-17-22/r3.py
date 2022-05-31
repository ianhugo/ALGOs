


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
need to model problem as a decision tree
O(b^d)
b = branching factor
d = depth

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
Partial solution:   a board with 0 to n queens
Root:       empty board
Children:   where to place next queen on next row
Leaves:     board with n queens
Dead Ends:  boards where two queens attack each other

Sudoku:
Nodes:      partially filled board
Root:       only given numbers
Children:   what digit to put in next cell
Leaves:     completely filled board
Dead ends:  boards with conflict
Iteration:  fill cells from top left, to bottom-right
(have to have traversal checking code)

Parenthese balanccing:
Nodes:      partially balanced parantheses
Root:       empty string
Children:   add ( or )
Leaves:     balanced paranthese string of size  n
Dead ends:  unbalanced 
            1: left parentheses open
            2: closed an unopened parentheses
Iteration:  put parenthese in next position

"""


def backtrack(partial):
    if dead_end(partial):
        prune()
        return
    
    if is_full(partial): #leave/full solution
        processing()
        print(partial)
    else:   #continue going
        for child in children(partial):
            backtrack(child)

"""
Subsets
= binary decision for each element

Root:       no decisions yet
Children:   take or not take this element
Leaves:     made decision on all elements
Dead ends:  no dead ends
Iterations: are we putting this element or not (each level)

O(2^n)

"""

def subset(L):
    backtracking([], 0, L)

def backtracking(picked, i, L):
    if i == len(L):
        print(picked)
    else:
        backtracking(picked+[L[i]], i+1, L)
        backtracking(picked, i+1, L)

"""
Permutations
Root:       empty list
Children:   what element to put next
Leaves:     every element in the list
Dead Ends:  none
Iterations: each level, add sth new

O(n!)
(N-queens, TSP . .. )
"""


def permutations(nums):
    backtracking([], nums)

def backtracking(perm, nums):
    if len(perm) == len(nums):
        print(perm)
        return
    
    for num in nums:
        if not num in perm:
            backtracking(perm=[num], nums)

"""
Optimizations:
1: represent partial solution smaller
2: store extra state, avoid recomputation
3: copy vs inplace

"""


"""
Dynamic Programming
1: Optimal substructure
optimal solution = optimal subproblems summed

2: Overlapping subproblem
subproblems repeated

similar to backtracking
but mapping to subproblem space instead
(have to pass parameters for targeting subproblem space)
(because have to store/reference the solution)

WHAT IS DP?
try all solutions
cache solutions

1: Top-Down
recurrence
(base case, passing down variables)

2: Bottom-up
use a matrix
(padding)


STEPS:
1. Analyze Recursion Tree
2. Brute Force
3. Cache Optimal States
    - add memo as argument
    - check for answers
    - store answers before return

Preprocessing   (base cases, pruning)
Processing      (spawn workers)
Postprocessing  (on return)

Preprocessing
Check Solutions (another base case, return immed)
Processing
Cache Solutions (after workers returned)
Postprocessing

"""



"""
Dynamic Programming: Bottom-up

to note:
1: index manipualtion
2: initialize DP table
3: pad base cases
4: build general cases
5: result in last cell
6: reconstruct soluution
"""

# Pathrise review complete
###############################################################



"""
Dikstra
Single source shortest path

0: have a visited array, a previous array, a distance array
1: start from a source
2: loop through edges
3: with edge x, compute new distance to node b, add in distance to current node 
4: if new distance, smaller than distance recorded in distance array, change
5: after looping, choose the lightest edge
6: repeat

no negative edges
because it closes edges/nodes
"""

import math

class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value #current lowest distnace value to reach this node


def dijkstra(start, end, adj):
    n = len(adj)

    dist = [math.inf] * n
    dist[start] = 0
    visited = [False] * n
    prev = [None] * n

    pq = deque()

    pq.append(Node(start, 0))

    while len(pq) != 0:
        node = pq.popleft()
        visited[node.id] = True

        if dist[node.id] < node.value:
            continue #node has been processed begtter

        for edge in adj[node.id]:
            if visited[edge.to]:
                continue
                
            new_dist = dist[node.id] + edge.cost

            if new_dist < dist[edge.to]:

                prev[edge.to] = node.id
                dist[edge.to] = new_dist

                pq.append(Node(edge.to, dist[edge.to]))
            
            if node.id == end:
                return dist[end], prev
    
    return math.inf, prev

"""
Bellman Ford
iterate V-1 times
update along all edges
can do negative edges, but no negative cycles
"""

def bellman(graph, v , start):

    dist =  [math.inf * v]
    dist[start] = 0
    prev = [None * v]

    for i in range(v-1):
        for edges in graph:
            for edge in edges:

                if dist[edge.pre] + edge.cost < dist[edge.to]:
                    dist[edge.to] = dist[edge.pre] + edge.cost
                    prev[edge.to] = edge.pre
    
    return prev

