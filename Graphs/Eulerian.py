"""
Eulerian path:
a path of edges
visit all edges in a grpah 
exactly once
depends on starting node

Eulerian circuit:
Eulerian path start and end at same vertex

undirected graph degree
directed graph in-degree and out-degree

Hierholtzer's algo
1: determine if Eulerian path exists
2: find starting node
starting: one extra out edge
ending: one extra in edge
3: modify DFS traverse good edges
stuck: no outgoing unvisited edges
backtrack, add current node to front of solution
call DFS on unvisited
until recursion unwinds to starting node

(take unvisited on backtrack until visited all)

NOTE: 
keep "out array", tracking number of outoing edges for each node
every time take edge
reduce outgoing edge count in "out array"
backtrack = check outarray if 0


"""
from Data_Structures import linked_list
#adj list, directed
class Eulerian_path_solver:
    def __init__(self, graph):
        self.graph = graph
        self.n = graph.size()
        self.path = linked_list.LinkedList()
        self.in_ed = []
        self.out_ed = []
        self.edge_count = 0
    
    def solve(self):
        self.set_up()

        if self.edge_count == 0:
            return None
        
        if not self.eulerian_exist():
            return None
        
        self.dfs(self.find_start_node())

        #make sure all edges traversed
        #could be disconnected
        if self.path.size != self.edge_count +1:
            return None
        
        sol = [None] * (self.n +1)
        while self.path.size > 0:
            sol[i] = self.path.remove_first()
        
        return sol



    def set_up(self):
        #loop through edges
        #increment, in and out degrees

        self.in_ed = [None]*self.n
        self.out_ed = [None]*self.n

        self.edge_count = 0

        for pre in range(self.n):
            for to in range(self.graph.get(pre)): #get edges
                self.in_ed[to] += 1
                self.out_ed[to] += 1
                self.edge_count += 1
    
    def eulerian_exist(self):
        #checking number of edges
        #checking numbe rof start_node, end_node for Eulerian exist
        #keep track of potential candidates
        #at most 1 for both
        start_nodes = 0 
        end_nodes = 0
        
        for i in range(self.n):
            if (self.out_ed[i] - self.in_ed[i] > 1) or (self.in_ed[i] - self.out_ed[i] > 1):
                return False
            elif self.out_ed[i] - self.in_ed[i] == 1:
                self.start_nodes += 1
            elif  self.in_ed[i] - self.out_ed[i] == 1:
                self.end_nodes += 1
        
        return (end_nodes == 0 and start_nodes == 0) or (end_nodes ==1 and start_nodes ==1)

        pass

    def find_start_node(self):
        start = 0

        for i in range(self.n):
            #unique starting node
            if self.out_ed[i] - self.in_ed[i] ==1:
                return i
            
            #start at node with outgoing edge
            if self.out_ed[i] > 0:
                start = i
        return start
    
    def dfs(self, at):
        #while still unvisited edges
        #visit next node recursively
        #when take edge, decrease outgoing edges for node
        #once empty, can add node to solution
        #out_ed is being used to keep track of how many left
        #as well as indexing to reach into adj list
        while self.out_ed[at] != 0:
            self.out_ed[at] -= 1
            next = self.graph.get(at).get(self.out_ed[at])
            self.dfs(next)
        
        self.path.add_first(at)