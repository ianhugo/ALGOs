from collections import deque


def print_orders(tasks, prerequisites):
    sortedOrder = []
    if tasks <= 0:
        return False

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
    graph = {i: [] for i in range(tasks)}  # adjacency list graph

    # b. Build the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1  # increment child's inDegree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    print_all_topological_sorts(graph, inDegree, sources, sortedOrder)

def print_all_topological_sorts(graph, inDegree, sources, sortedOrder):
    if sources:
        for vertex in sources:
            sortedOrder.append(vertex)
            sources_next = deque(sources) #copy

            sources_next.remove(vertex) #remove current
            
            for child in graph[vertex]: #normal decrement
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources_next.append(child)
            
            #recursive call for remaining and new "sources"
            print_all_topological_sorts(graph, inDegree, sources_next, sortedOrder)

            #backtrack
            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] += 1
    
    #only print at top level
    #only print when have a valid ordering
    if len(sortedOrder) == len(inDegree):
        print(sortedOrder)