"""
non-negative edges

uses DFS

dist array
* distance to every node = positive infinity
* mark distance to start node “s” = 0

Priority Queue
* (node-index, distance)
* insert (s, 0) to start

“parent” array
* keep track of for this node, which node came previously, for the current shortest path

“visited” array or hash
* keep track of if node has been visited

Iteration
* pull out next node (lowest distance)
* iterate over all edges outward (visit all neighbors)
* visit node v
* update dist array for node v (relax each edge)
* append visited (node, distance) to PQ
* pop off the node we visited from
* poll pq and repeat
"""
import math
from collections import deque

class Edge:
    def __init__(self):
        self.to = None
        self.pre = None
        self.cost = None

class Node:
    def __init__(self):
        self.id = None
        self.value = None

#adj list
#assumes with node objects, the value, is initialized to current lowest
def dijkstra(start, end, adj):
    n = len(adj)
    dist = [math.inf]*n

    dist[start] = 0
    visited = [False]*n
    prev = [None]*n

    pq = deque()            #this is not a priority queue
    #degree = edgeCount / n
    #can use indexed PQ as well

    pq.append(Node(start, 0))

    while len(pq) != 0:
        node = pq.popleft()
        visited[node.id] = True

        if dist[node.id] < node.value:  #if already found better distance
            continue

        for edge in adj[node.id]:   #get all edges
            if visited[edge.to]:    #if already visited, can't get lower
                continue

            newdist = dist[node.id] + edge.cost #grabbing curr optimal, add edge cost

            if newdist < dist[edge.to]:
                prev[edge.to] = node.id
                dist[edge.to] = newdist

                pq.append(Node(edge.to, dist[edge.to]))
                #if ipq, then check if in queue, if so update, if not insert
            
            if node.id == end:
                return dist[end], prev
    
    return math.inf, prev


def reconstruct_path(start, end, prev, adj):
    n = len(adj)
    if end < 0 or end >=n:
        print("error")
    
    dist, prev = dijkstra(start, end, adj)
    path = []

    if dist == math.inf:
        return path
    
    at = end
    while at != None:
        path.append(at)
        at = prev[at]
    path.reverse()
    return path
    

## better implementation

import heapq

def dijkstra(G: nx.Graph, w:DefaultDict,  s) ->Tuple[Dict,Dict]:
    distances, parents = defaultdict(lambda : np.Inf), defaultdict(lambda:s)
    Q = []

    #set source, node-id
    distances[s] = 0
    parents[s] = None

    visited_nodes = set()

    #append with tuple, (distances[v]. vertex-id) )
    Q.append( (distances[s], s))
    heapq.heapify(Q)

    while Q != []:
        current_node = heapq.heappop(Q)
        current_node_id = current_node[1]
        current_node_dist = current_node[0]

        visited_nodes.add(current_node_id )   #put node-id into set
        for each in G.adj[current_node_id]:
            adj_node_id = each
            if adj_node_id not in visited_nodes:
                if distances[current_node_id] < current_node_dist: #skip if a stale node, already achieved shorter distances
                    continue
                else:
                    w = G.adj[current_node_id][adj_node_id]["weight"]
                    relax(w, current_node_id, adj_node_id, distances, parents)
                    new_heap_item = (distances[adj_node_id], adj_node_id)
                    heapq.heappush(Q, new_heap_item)
    #TODO
    return distances,parents

def relax(w, u, v, distances, parents) -> None:
    #TODO
    if distances[v] > distances[u] + w:
        distances[v] = distances[u] + w
        parents[v] = u
    pass