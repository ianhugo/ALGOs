"""
Leetcode 210: Course Schedule 2
solve with DFS

IDEA: 
- find source node A
- consider all path stemming from A
- finish up recursion for A
- move on from A

- all node starting from A, has A as ancestor

1. initialize stack
2. construct adj list
3. for each node, run DFS
4. recursively traverse all neighbors of node (backtrack)
5. add node to stack
6. all nodes that need node, already in stack

add node to stack: when can go no further
- leaf
- no other unvisited node

"""

class Solution:

    White = 1      #unvisited
    Gray = 2       #currently visiting
    Black = 3      #finished, added to solution

    def find_order(self, num, pre):
        """
        pre = [ [a, b], [b, c] . . .]
        a is a pre-req for b

        num = number of nodes
        """

        adj_list = {}

        #initialize
        for src, dest in pre:
            adj_list[src].append(dest)
        
        top_sort = []
        is_possible = True

        #mark all vertices as white
        color = {k: Solution.White for k in range(num)}

        def dfs(node):
            nonlocal is_possible

            #stop early if found cycle
            if not is_possible:
                return
            
            #start recursion
            color[node] = Solution.Gray

            #traverse neighbors
            if node in adj_list:
                for neighbor in adj_list[node]:
                    #if unvisited
                    if color[neighbor] == Solution.White:
                        dfs(neighbor)
                    #edge to gray vertex = cycle
                    elif color[neighbor] == Solution.Gray:
                        is_possible = False
            
            #end recursion success
            color[node] = Solution.Black
            top_sort.append(node)

        
        for vertex in range(num):
            #if unprocessed node, call dfs
            if color[vertex] == Solution.White:
                dfs(vertex)
        
        return top_sort[::-1] if is_possible else []