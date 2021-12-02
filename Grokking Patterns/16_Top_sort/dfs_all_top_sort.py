"""
after returning from function
reset values of visited, result, indegree

"""

class Graph:
    def __init__(self, edges, N):
        self.adj_list = [[] for _ in range(N)]

        self.in_degree = [0] * N

        for (src, dest) in edges:

            #add edge
            self.adj_list[src].append(dest)
            
            #increment in_degree
            self.in_degree[dest] = self.in_degree[dest] +1
    

def print_all_top_sort(graph):
    N = len(graph.adj_list)

    #whether vertices discovered
    discovered = [False] * N

    #storing path
    path = []

    find_all_top_sort(graph, path, discovered, N)

def find_all_top_sort(graph, path, discovered, N):

    #process every vertex
    for v in range(N):
        
        #proceed if in_degree of current is 0
        #current not processed yet

        if graph.in_degree[v] == 0 and not discovered[v]:
            
            #every neighbor
            for u in graph.adj_list[v]:
                graph.in_degree[u] -= 1
            
            path.append(v)  #current node in path

            discovered[v] = True #mark as discovered

            #recur
            find_all_top_sort(graph, path, discovered, N)

            #backtrack reset
            for u in graph.adj_list[v]:
                graph.in_degree[u] += 1
            
            path.pop()
            discovered[v] = False
    
    #print at top level
    #only valid ones
    if len(path) == N:
        print(path)