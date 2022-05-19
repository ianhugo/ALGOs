"""
Algorithms are about problem-solving
we have a set of tools in our toolbox
how do we adapt it to the context and problem-solve

Communication
Problem-solving
Coding
Verification

What is the input
What is the output
What property to track?
What data structure to store?
Which tool, and which type of it?

"""


"""
Bellman Ford
shortest path on weighted graph
can handle negative edges
(no algo can do negative cycles)
"""

import math

def bellman(graph, v, start):

    dist = [math.inf]*v
    dist[start]= 0
    prev = [None] * v

    for i in range(v-1):
        for edges in graph:
            for edge in edges:

                if dist[edge.pre] + edge.cost < dist[edge.to]:
                    dist[edge.to] = dist[edge.pre] + edge.cost
                    prev[edge.to] = edge.pre

    return prev


"""
Dijkstra
shortest path on weighted graph

start from starting node
update the dist array for all reachable nodes

choose the smallest edge

repeat


What is the input: source, destination
What is the output: shortest distance, prev array
What property to track? distance array, visited array, prev array, to_visit array
What data structure to store? arrays, node class to store 
Which tool, and which type of it? loop over an array

"""

from collections import deque

class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value

def dijkstra(start, end, adj):
    n = len(adj)

    dist = [math.inf]*n

    dist[start] = 0
    visited = [False]*n
    prev = [None]*n

    pq = deque()

    pq.append(Node(start,0))

    while len(pq) != 0:
        node = pq.popleft()
        visited[node.id] = True #mark as processed

        if dist[node.id] < node.value:  #prevent double/redundant process
            continue

        for edge in adj[node.id]:   #consider all edges, coming from this node
            if visited[edge.to]:    #if the target node, is visited, skip
                continue
            
            #compute new distance
            newdist = dist[node.id] + edge.cost

            #if using this edge, the distance is lower than current
            if newdist < dist[edge.to]:

                #update prev and distance
                prev[edge.to] = node.id
                dist[edge.to] = newdist

                #append to queue, as this is processed and 
                pq.append(Node(edge.to, dist[edge.to]))
            
            if node.id == end:  #reached the end
                return dist[end], prev
    
    return math.inf, prev


"""
BFS

shortest path on unweighted graph
layer by layer
"""


class BFS_solver:

    def __init__(self, graph, nodes):
        self.len = nodes
        self.visited = [False] * self.len
        self.prev = [None] * self.len
        self.queue = deque()
        self.graph = graph
    
    def bfs(self, start, end):
        prev = self.solve_bfs(start)
        self.reconstruct_path(start, end, prev)
    
    def solve_bfs(self, start):
        self.visited[start] = True
        self.queue.append(start)

        while not len(self.queue) == 0:
            node = self.queue.append(next)
            neighbors = self.graph[node].neighbors

            for next in neighbors:
                if not self.visited[next]:
                    self.queue.append(next)
                    self.visited[next] = True
                    self.prev[next] = node
        return self.prev
    
    def reconstruct_path(self, start, end, prev):
        path = []
        node = end
        while node != None:
            path.append(node)
            node = prev[node]
        
        path.reverse()

        if path[0] == start:
            return path
        return []


"""
DFS

INPUT
OUTPUT
TRACK: visited
DATA-STRUCT: stack
PATTERN:
PATTERN CONTEXT:
COMPLEXITY


"""

def dfs(graph, start, n):

    count = 0
    visited = [False]*n
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


"""
problem-solving:
DECISION TREE: partial solutions?

ROOT: start with?
CHILDREN: what is the decision?
LEAVES: what is the full solution?
DEADENDS: what is an invalid solution?

implementation:
PREPROCESSING
PROCESSING
SELECTION
POSTPROCESSING
VARIABLES
"""
def dfs_recur(at, visited, graph):

    if visited[at]:
        return
    
    visited[at] = True
    count = 1
    edges = graph[at].edges

    if edges != []:
        for edge in edges:
            count += dfs(edge.to, visited, graph)
    
    return count