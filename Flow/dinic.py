"""
unweighted bipartite matching
building level graph
combining traversal techniques
introducing a blocking flow

strongly polynomial, max flow
O(V^2 E)
does not depend on capacity of graph

on bipartite graph
O(sqrt(VE))
can do huge graphs
(reduction to Hopcroft-Karp)
(standard to competitive programming)

INTUITION:
make continuous positive progress toward goal
guide augmenting paths with "level graph"

LEVELS = BFS from source
backwards or sideways level paths are avoided

residual edges must be positive direction
must have remaining capacity >0

1: construct level graph, with BFS, label levels
2: if sink not reached, stop, return max flow
3: using only valid edges, DFS until reach blocking flow
    (backtrack when dead end)
4: max flow = sum over bottleneck values of all augmenting paths
5: repeat, rebuild level graph with available capacity eges

blocking path = does not exist any more paths from s-> t
(if bipartite, get maximum matching)

NEED: prune dead ends, when backtracking during DFS

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
    
class Dinics_solver:
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
        self.graph = graph #adj list?
        self.level = [None]*self.num_nodes
    
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
        #keep building level graph, then do dfs
        
        #pruning mechanism
        #list of edges leaving a node can be indexed to node
        #skip edges leading to dead end
        #tracking for each node, which is a non-dead end edge
        self.next = [0] * self.num_nodes

        while self.bfs():
            #reset next array, allow previously forbidden edges
            self.next = [0] * self.num_nodes
            f = self.dfs(self.source, self.next, math.inf)
            while f!= 0:
                self.max_flow += f
                f = self.dfs(self.source, self.next, math.inf)
            pass
    
    def bfs(self):
        #compute depth/level of each node
        #level = min number of edges from node to source
        self.level = [-1] * self.num_nodes
        q = deque()
        q.append(self.source)
        self.level[self.source] = 0
        while q != []:
            node = q.popleft()
            if node == self.sink:
                break
            for edge in self.graph[node].edges:
                cap = edge.remain_capacity()
                #have capacity, and is unvisited
                if (cap > 0) and self.level[edge.to]==-1:
                    self.level[edge.to] = self.level[node] +1
                    q.append(edge.to)
        return self.level[self.sink] != -1 #able to reach sink?

    def dfs(self, at, next, flow):
        #current node, next array, min flow along path so far
        #recursive
        if at == self.sink:
            return flow

        num_edges = self.graph[at].size() #number of edges outwards

        while next[at] < num_edges:
            edge = self.graph[at].get(next[at]) #get the next edge
            capacity = edge.remain_capacity()
            next[at] += 1
            #has capacity, and goes up a level
            if capacity > 0 and (self.level[edge.to] == (self.level[at]+1)):
                bottleneck = self.dfs(edge.to, next, min(flow, capacity))
                #recursive
                #now unwind
                if bottleneck >0: #found augmenting path
                    edge.augment(bottleneck)
                    return bottleneck
            
            next[at] += 1
            #if it is a dead end, it was visited, 
            # and incremented, will not be visited again
        
        return 0