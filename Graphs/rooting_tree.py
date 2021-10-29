"""
put in undirected graph, root it with a particular node
an adjacency list with undirected edges
root_id = make that node id root
"""

class Tree_Node:

    def __init__(self, id, parent, children):
        self.id = id
        self.parent = parent      #root node this remains none
        self.children = children


def root_tree(graph, root_id = 0):
    root = Tree_Node(root_id, None, [])
    return build_tree(graph, root, None)

def build_tree(graph, node, parent):
    for child_id in graph(node.id):

        #prevent edge going back to parent
        if parent != None and child_id == parent.id:    
            continue
        #othersie, proper child node
        child = Tree_Node(child_id, node, [])
        node.children.append(child)
        build_tree(graph, child, node)
    return node