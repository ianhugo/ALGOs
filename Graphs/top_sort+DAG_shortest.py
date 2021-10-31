"""
many things can be modelled as a graph

1. Single Source Shortest path on DAG
Top sort the DAG
iterate through in Top-Sort order, do BFS
set
update a shortest-path array
keep relaxing if find a shorter path

2. Single Source Longest path on DAG 
O(V+E)
multiply each edge by -1
do shortest path
then multiply all by -1 again

"""
import math

#adjacency list


def dfs(i, at, visited, ordering, graph):
    visited[at] = True

    edges = graph[at].edges

    if edges != []:
        for edge in edges:
            if not visited[edges.to]:
                i = dfs(i, edge.to, visited, ordering, graph)
    
    ordering[i] = at
    return i - 1

def top_sort(graph, num_nodes):
    ordering = []
    visited = []

    i = num_nodes - 1

    at = 0
    while at < num_nodes:
        if not visited[at]:
            i = dfs(i, at, visited, ordering, graph)
    
    return ordering

def dag_shortest(graph, start, num_nodes):
    topsort = top_sort(graph, num_nodes)
    dist = [math.inf] * num_nodes
    dist[start] = 0
    prev = []

    #if start not source node, skip index values in topsort array
    #as everything left of the source would not be reached
    for i in range(num_nodes):
        node_idx = topsort[i]
        if dist[node_idx] != None:
            adj_edges = graph[node_idx]
            if adj_edges != []:
                for edge in adj_edges:  #bfs
                    newdist = dist[node_idx] + edge.weight

                    #relaxation
                    if dist[edge.to] == None:
                        dist[edge.to] = newdist
                        prev[edge.to] = edge.pre
                    else:
                        dist[edge.to] = min(dist[edge.to, newdist])
                        if dist[edge.to] == newdist:
                            prev[edge.to] = edge.pre

    return dist, prev

#adjacaency matrix

def top_sort_matrix(matrix):
    n = len(matrix)
    visited = [False]*n
    order = [None]*n
    index = n-1

    for u in range(n):
        if not visited[u]:
            index = dfs_matrix(matrix, visited, order, index, u)
    
    return order

def dfs_matrix(matrix, visited, order, index, u):

    if visited[u]:
       return index
    visited[u] = True

    for v in range(len(matrix)):    #visit neighbors
        if (matrix[u][v] != None) and (not visited[v]):
            index = dfs_matrix(matrix, visited, order, index, v)
    
    order[index] = u    #place at head of list

    return index - 1

def dag_shortest_matrix(matrix, start):
    n = len(matrix)
    dist = [math.inf]*n
    dist[start] = 0
    prev = []

    for u in top_sort_matrix(matrix):
        for v in range(n):
            if matrix[u][v] != None:
                newdist = dist[u] + matrix[u][v]
                if newdist < dist[v]:
                    dist[v] = newdist
                    prev[v] = u
    return dist, prev
