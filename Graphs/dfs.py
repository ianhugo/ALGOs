
"""
O(V+E)

plunge depth-first
"""

from collections import deque

def dfs(graph, start, n):
    #n = number of nodes

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


#counting number of nodes traversed
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