"""
Flow graph: each edge has maximum capacity, directed edges
Flow value: amount passing through that edge 
Max flow: how much capacity can flow through a graph

Can represent many types of things (many applications)
A source
A sink
max flow = maximum going out of source, coming into sink

Augment paths, through a RESIDUAL graph
augments until no more augmenting paths found

Augmenting path:
path of edge, in residual graph (source to sink)
with unused capacity

Augmenting path has Bottlenecks
the smallest capacity edge on the graph
Use capacity on Bottleneck, to augment the flow

Augment = updating flow value of
edges on augmenting path


Residual graph = copy of graph's nodes
= each directed edge, has a reversed edge

same direction edge = remaining capacity of edge
in real rgaph

reverse direction edge = used capacity of edge
in real graph

GOAL = find augmenting path in residual graph
then update real graph
Why works = simple path in residual grpah, 
can contain reversed edges, can flow through
can redistribute flow, decreasing flow on some

Max flow Min cut=
stopping condition of Ford Fulkerson
if cut the graph, partition
the edges on which the cut happens
a min cut is where the cut hits edges, which total
to a minimum capacity among other cuts of edges
at this cut, there is a maximum amount of flow

NOTE:
does not specify how to find augmenting path
can optimize here

O(E * f)
complexity depended on capacity of graphs

"""

#set up edges from source
#set up mid edges
#set up edges to sink

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
    
class Ford_Fulkerson_solver:
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
        self.visited = [None]*self.num_nodes

        self.solved = False
        self.max_flow = None
        self.graph = graph
    
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
        f = self.dfs(self.source, math.inf)
        while f!= 0:
            self.visited_token += 1
            self.max_flow += f
            f = self.dfs(self.source, math.inf)

    
    #start at infinity
    #as go through graph, flow becomes bottlneck value
    def dfs(self, node, flow):
        if node == self.sink:
            return flow
        
        self.visited[node] = self.visited_token

        edges = self.graph[node]
        for edge in edges:
            rr = edge.remain_capacity()
            #can push flow through
            #can avoid cycle
            if (rr > 0) and (self.visited[edge.to] != self.visited_token):
                #if this new edge is bottleneck
                #should become bottleneck value
                #happens recursively, until reach sink
                bottleneck = self.dfs(edge.to, min(flow, rr))
                
                #now augment
                #propagate up the stack
                #other edges augment
                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck
        return 0

# class Ford_Fulkerson_solver:
#     def __init__(self, graph, sink, source):
#         self.num_nodes = None
#         self.source = self.num_nodes -1
#         self.sink = self.num_nodes -2