"""
a heuristic

should push flow through largest edges
then use smallest edge
achieve max flow quicker
(Ford Fulkerson can have augmenting
capacity 1, O(f, e))

don't want to augment by only 1 unit
prioritize large capacity edges

U = value of largest edge capacity
do max

D = largest power of 2, <= U

only take edges, 
with remaining capacity >= D

once cannot find more of such
D = D/2
repeat while D >0


with DFS
O(E^2 lg u)

or
O(EV log U)
(for shortest augmenting path)

(but DFS with capacity scaling 
seems a bit faster in practice)

"""



import math

class Edge:
    def __init__(self, pre, to, capacity):
        self.pre = pre
        self.to = to
        self.residual = None #an edge
        self.flow = None
        self.capacity = capacity
    
    def is_residual(self):
        return self.capacity == 0
    
    def remain_capacity(self):
        return self.capacity - self.flow
    
    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck
    
class Ford_Fulkerson_solver_cap_scaling:
    def __init__(self, num_nodes, source, sink, graph):
        self.num_nodes = num_nodes
        self.source = source
        self.sink = sink
        self.delta = None   #determine whether edge accepted

        #accelerates, tracks visited state
        #when find augmenting path
        #don't want to visit same nodes twice
        #avoid cycle
        #check if visited[i] == visited_token
        self.visited_token = 1
        self.visited = [None]*self.num_nodes

        self.solved = False
        self.max_flow = None
        self.graph = graph
    
    def mark_all_unvisited(self):
        self.visited_token += 1

    def add_edges(self, pre, to, capacity):
        if capacity <= 0:
            print("bad arg")
        
        e1 = Edge(pre, to, capacity)    #residual graph edge
        e2 = Edge(to, pre, capacity)    #reversed

        e1.residual = e2
        e2.residual = e1

        self.graph[pre].add(e1)
        self.graph[to].add(e2)
        self.delta = max(self.delta, capacity) #CAP SCALING

    def solve(self):
        
        #CAP SCALING
        #start delta at largest power of 2 <= largest capacity
        self.delta = math.floor(math.log(self.delta, 2)) ** 2

        f = self.dfs(self.source, math.inf)
        
        while self.delta > 0:
            while f!= 0:
                self.visited_token += 1 #self.mark_all_unvisited()
                self.max_flow += f
                f = self.dfs(self.source, math.inf)
            self.delta /= 2

    
    #start at infinity
    #as go through graph, flow becomes bottlneck value
    def dfs(self, node, flow):
        if node == self.sink:
            return flow
        
        self.visited[node] = self.visited_token

        edges = self.graph[node]
        for edge in edges:
            rr = edge.remain_capacity()
            #can push flow through
            #can avoid cycle
            #CAP SCALING : if statement, contains capacity scaling
            if (rr >= self.delta) and (self.visited[edge.to] != self.visited_token):
                #if this new edge is bottleneck
                #should become bottleneck value
                #happens recursively, until reach sink
                bottleneck = self.dfs(edge.to, min(flow, rr))
                
                #now augment
                #propagate up the stack
                #other edges augment
                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck
        return 0