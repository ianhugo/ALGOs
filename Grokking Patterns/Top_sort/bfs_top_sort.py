"""
Given: directed graph
Want: top ordering of vertices

IDEA:
1. find all sources
2. add to sorted list
3. decrement all children
4. If child in-degree == 0, enqueue
5. Repeat until Queue is empty

"""

from collections import deque

def top_sort(vert, edg):
    sorted = []

    if vert <= 0:
        return sorted
    
    #initialize graph
    in_degree = {i: 0 for i in range(vert)}
    graph = {i: [] for i in range(vert)}

    #build graph/populate
    for edge in edg:
        parent, child = edge[0], edge[1]
        graph[parent].append(child) #put into parent list
        in_degree[child] += 1 #increment indegree
    
    #find sources
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)
    
    #for each source, add to sorted
    #subtract 1 from child in in_degree
    #if in_degree = 0, add to sources queue
    while sources:
        vertex = sources.popleft()
        sorted.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    
    #impossible to top sort
    #theres a cycle
    if len(sorted) != vert:
        return []

    return sorted
    
