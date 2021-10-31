"""

Strongly Connected Component
* self-contained cycle
* every vertex in cycle, can reach every other cycle

low-link value
* smallest node id, reachable from that node with DFS (including own node)

Label each node with their low-link value
dependent on traversal order

Tarjan’s
* stack of valid nodes, from which to update low-link value from node
* added to stack, when first explored
* removed from stack, when SCC found
* update low-link value on the fly
* O( V + E)

Condition of update:
if exploring u
if there is path from u to v
if node v is on stack
then can update u to have low link value of v’s (min with)

PROCEDURE
1. mark all nodes unvisited
2. start DFS until visit all
3. when visit, assign id, low-link = id
4. mark it as visited, put it on stack
5. when hit visited, recursion back
6. if previous node (visited from 5) is on stack, min(current node low-link, last node low-link)
7. if current node id = low-link, and has visited all neighbors, pop off associated nodes from stack
"""
from collections import deque


class Tarjan_solver:
    def __init__(self, graph):
        self.graph = graph
        self.lent = len(graph)
        self.solved = False
        self.component_count = 0
        self.node_id = 0
        self.id = [None] * self.lent
        self.low_link = [None] * self.lent
        self.on_stack = [False] * self.lent
        self.stack = deque()
        self.solve()

    
    def solve(self):
        for i in range(self.lent):
            if not self.visited[i]:
                self.dfs(i)
    
    def dfs(self, at):
        self.stack.append(at)
        self.on_stack[at] = True
        id = self.node_id   #assigning id
        self.node_id += 1
        self.id[at] = id
        self.low_link[at] = id

        #iterate over neighbors
        for to in self.graph[at].neighbors:
            if self.id[to] == None:
                self.dfs(to)
            
            if self.on_stack[to]:
                self.low[at] = min(self.low[at], self.low[to])
        
        #recursive callback
        #if at root node of starting component
        #empty the stack
        if self.id[at] == self.low[at]:
            hit = False
            while not hit:
                node = self.stack.pop()
                self.on_stack[node] = False
                self.low_link[node] = self.id[at]
                if node == at:
                    hit = True
                    break
            self.component_count += 1



