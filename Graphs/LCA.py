
from Data_Structures import sparse_table

class Tree_Node:
    def __init__(self, index, parent, children = []):
        self.subtree_sz = None
        self.id = index   #or id
        self.parent = parent
        self.children = children
    
def root_tree(graph, root_id = 0):
    root = Tree_Node(root_id, None, [])
    rooted_tree = build_tree(graph, root)

    if rooted_tree.subtree_sz < graph.size: #graph needs size attribute
        print("Missing edges")
    return rooted_tree

def build_tree(graph, node):
    subtree_node_count = 1
    for neighbor in graph(node.id):

        #prevent edge going back to parent
        if node.parent != None and neighbor == node.parent.id:    
            continue
        #othersie, proper child node
        child = Tree_Node(neighbor, node, [])
        node.children.append(child)
        build_tree(graph, child)
        subtree_node_count += child.subtree_sz
    node.subtree_sz = subtree_node_count
    return node

class LCA_euler:
    """visit dfs all nodes, to and back, populate arrays"""
    def __init__(self, root):
        self.subtree_sz = root.subtree_sz
        self.node_order = []
        self.node_depth = []
        self.last = []
        self.tour_index = 0
        self.setup(root)
        pass

    def setup(self, root):
        self.euler_tour_size = 2 * self.subtree_sz - 1
        self.node_order = [None]*self.euler_tour_size
        self.node_depth = [None]*self.euler_tour_size
        self.last = []*self.subtree_sz

        self.dfs(root, 0)
        self.sparse_table = sparse_table.Sparse_Table()
        self.sparse_table.operation = "MIN"
        self.sparse_table.init(self.node_depth)
    
    def dfs(self, node, depth): #eulerian tour
        if node == None:    #base case
            return
        
        self.visit(node, depth)
        for each in node.children:
            self.dfs(each, depth+1)
            self.visit(node, depth)
    
    def visit(self, node, depth):
        self.node_order[self.tour_index] = node
        self.node_depth[self.tour_index] = depth
        self.last[node.id] = self.tour_index
        self.tour_index += 1
    
    def lca(self, idx1, idx2):
        l = min(self.last[idx1], self.last[idx2])
        r = max(self.last[idx1], self.last[idx2])
        i = self.sparse_table.query_index(l, r)
        return self.node_order[i]


def main():
    solver = LCA_euler(root)


    lca = solver.lca(13, 14)