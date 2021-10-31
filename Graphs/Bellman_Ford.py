"""
O(VE)
can do negative cycles (can find negative cycles)
relax V-1 times

do BFS on each edge

if run V-th time, and still relax, we can find the negative cycles
"""

import math

#adjcaency List

def bellman_ford(graph, v, start):

    #v = number of nodes

    dist = [math.inf]*v
    dist[start] = 0
    prev = [None]*v

    for i in range(v-1):
        for edges in graph:
            for edge in edges:
                if dist[edge.pre] + edge.cost < dist[edge.to]:
                    dist[edge.to] = dist[edge.pre] + edge.cost
                    prev[edge.to] = edge.pre
    
    #finding negative cycles
    for i in range(v-1):
        for edges in graph:
            for edge in edges:
                if dist[edge.pre] + edge.cost < dist[edge.to]:
                    dist[edge.to] = - math.inf

    return dist