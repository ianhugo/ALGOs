"""
dense graph with lots of edges

lazy: O(E lg E)
eager: O(E lg V)

1. PQ on min edge cost
2. start at any node, iterate over edges, add to PQ
3. while PQ not empty, MST not formed
4. dequeue next cheapest edge
5. if outdated (points to a node already visited), poll again
6. else, mark node as visited, add selected edge to MST
7. visit the new node

"""


class Prim_solver:
    def __init__(self, graph):
        self.graph = graph
        self.size = graph.size()
        self.solved = False
        self.mst_exist = False
        self.visited = []
        self.priority_queue = []
        self.min_cost = None
        self.mst = []
    
    def solve(self):
        if self.solved:
            return
        
        expected_edges = self.size -1
        edge_count = 0

        self.priority_queue = [] #initialize priority queue here

        #initial relax set of edges, for
        self.relax_edges_at(0)

        while not self.priority_queue == [] and edge_count != expected_edges:
            dest_node, edge = self.priority_queue.poll()  #get cheapest edge
            self.mst.append(edge)
            self.min_cost += edge.cost

            self.relax_edges_at(dest_node)
        
        self.mst_exists = (edge_count == expected_edges)
    
    def relax_edges_at(self, idx):
        self.visited[idx] = True
        out_edges = self.graph.edges[idx]

        for edge in out_edges:
            dest_node = edge.to

            #skip edges of already visited nodes (already in MST)
            if self.visited[dest_node]:
                continue
            
            #relaxing edges
            if self.priority_queue.contains(dest_node):
                #decrease node related weight in queue
                self.priority_queue.decrease(dest_node, edge)
            else: #insert edge for first time
                self.priority_queue.insert(dest_node, edge)

