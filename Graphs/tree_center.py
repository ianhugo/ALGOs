"""
good for finding a good node to root tree
one or two centers max

middle or middle two vertices
in longest path along tree

1. compute degree of each node
(nodes neighboring)
2. prune lowest degree, update degree
3. eventually reach center of tree

"""


def tree_center(graph):
    n = graph.num_nodes()
    degree = [0] * n
    leaves = []

    for i in range(n):
        edges = graph.get(i)    #get edges of i
        degree[i] = edges.size()
        if degree[i] <= 1:
            leaves.append(i)
            degree[i] = 0
    
    count = len(leaves)

    while count < n:
        new_leaves = []
        for node in leaves:
            for neighbor in graph.get(node):
                degree[neighbor] -= 1   #as removing current node
                if degree[neighbor] ==1:
                    new_leaves.append(neighbor)
            degree[node] = 0 #finish pruning leave node
        count += len(new_leaves)
        leaves = new_leaves
    
    return leaves
