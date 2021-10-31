"""
Indexed edges
hash: (node -> group)


1. sort edges by ascending edge weight
2. walk through sorted edges, look at two node of the edge
	1. if nodes already unified, skip edge
	2. otherwise include it, unfy nodes/groups
3. terminate whene very edge proceesed or all vertices unified
	1. depends on if want Minimum spanning tree or forest

PATH COMPRESSION
make nodes of same group, point to one particular node, 
or have a particular group id

"""

class Union_find:
    def __init__(self, size):
        self.size = size
        self.sz = [None]*size
        self.id = [None]*size    #points to parent node, if id[i] = i, root node
        self.component_count = None

        for i in range(size):
            self.id[i] = i  #link each to itself
            self.sz[i] = 1

    #given node, find which component belonging
    def find(self, p):
        root = p
        while root != self.id[root]:    #when found self loop
            root = self.id[root]
        
        #path compression
        while p != root:
            next_up = self.id[p]
            self.id[p] = root
            p = next_up
        
        return root
    
    #are these same component?
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    #unify two components
    def unify(self, p, q):

        #find root nodes
        root1 = self.find(p)
        root2 = self.find(q)

        if root1 == root2:
            return
        
        if self.sz[root1] < self.sz[root2]: #unify . .
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
        
        self.component_count -= 1


class Kruskal_solver:
    def __init__(self, graph):
        self.graph = graph
        self.sum = 0
    
    def solve(self):
        
        #sort edges by ascending weights
        edges = []

        num_nodes = self.graph.size()
        uf = Union_find(num_nodes)

        for edge in edges:
            if uf.connected(edge.pre, edge.to):
                continue
                
            uf.unify(edge.pre, edge.to)
            self.sum += edge.cost

            if uf.size[0] == num_nodes:
                break

        if uf.size[0] != num_nodes:
            return None
        
        return self.sum


