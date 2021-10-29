"""

O(V+E)

shortest path on unweighted graphs

explore neighbors layer by layer

uses a queue
"""
from collections import deque

class Edge:
    def __init__(self, pre, post, cost):
        self.pre = pre
        self.post = post
        self.cost = cost

class BFS_util:
    def __init__(self, graph):
        self.len = 0 #number of nodes
        self.visited = [False] * self.len 
        self.prev = [None] * self.len
        self.queue = deque()
        self.graph = graph

    def bfs(self, start, end):
        prev = self.solve_bfs(start)
        self.reconstruct_path(start, end, prev)

    def solve_bfs(self, start):
        #assume pass in index
        n = 1 #max number of nodes in graph
        self.visited[start] = True
        self.queue.append(start)

        while not len(self.queue) == 0:
            node = self.queue.popleft()
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



