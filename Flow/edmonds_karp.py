"""
Instead of DFS, use BFS

O(V * E^2)

does not depend on capacity of edges
= a strongly-polynomial algo

find shortest augmenting path from s->t

why not DFS:
longer path = higher chance, small bottleneck value
= longer runtime

with BFS:
shorter paths
reduce length of augmenting paths

1. enqueue all reachable neighbors
2. stop at sink, for any edge
3. find bottleneck, as smallest remaining capacity
4. update in "real" graph

"""
from collections import deque
import math

class Edge:
    def __init__(self, pre, to, capacity):
        self.pre = pre
        self.to = to
        self.residual = None #an edge
        self.flow = None
        self.capacity = capacity
    
    def is_residual(self):
        return self.capacity == 0
    
    def remain_capacity(self):
        return self.capacity - self.flow
    
    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck
    
class Edmond_Karps_solver:
    def __init__(self, num_nodes, source, sink, graph):
        self.num_nodes = num_nodes
        self.source = source
        self.sink = sink

        #accelerates, tracks visited state
        #when find augmenting path
        #don't want to visit same nodes twice
        #avoid cycle
        #check if visited[i] == visited_token
        self.visited_token = 1
        self.visited_ar = [None]*self.num_nodes

        self.solved = False
        self.max_flow = None
        self.graph = graph
    
    def visit(self, i):
        self.visited_ar[i] == self.visited_token
    
    def visited(self, i):
        return self.visited_ar[i] == self.visited_token
    
    def mark_all_unvisited(self):
        self.visited_token += 1
    
    def add_edges(self, pre, to, capacity):
        if capacity <= 0:
            print("bad arg")
        
        e1 = Edge(pre, to, capacity)    #residual graph edge
        e2 = Edge(to, pre, capacity)    #reversed

        e1.residual = e2
        e2.residual = e1

        self.graph[pre].add(e1)
        self.graph[to].add(e2)

    def solve(self):
        f = self.bfs()
        while f!= 0:
            self.mark_all_unvisited()
            self.max_flow += f
            f = self.bfs()

    def bfs(self):
        q = deque()
        self.visited(self.source)
        q.append(self.source)

        self.prev = [None] * self.num_nodes

        while q != []:
            node = q.popleft()
            if node == self.sink:
                break

            for edge in self.graph[node].edges:
                cap = edge.remain_capacity()
                if (cap > 0) and not self.visited(edge.to):
                    self.visit(edge.to)
                    self.prev[edge.to] = edge
                    q.append(edge.to)
        
        #sink not reachable
        if self.prev[self.sink] == None:
            return 0
        
        #augmenting path exist
        #trace back through prev array
        bottleneck = None

        edge = self.prev[self.sink]

        while edge != None:
            bottleneck = min(bottleneck, edge.remain_capacity())
            edge = self.prev[edge.pre]
        
        edge = self.prev[edge.pre]
        while edge != None:
            edge.augment(bottleneck)
        
        return bottleneck


