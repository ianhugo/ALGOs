"""
structurally the same, different orientation/labels

bijection between nodes

NP complete 
polynomial for graph subclasses tho: trees

probabilistic: hash or heuristic based

serializing a tree -> unique encoding

try rooting with same root nodes before serializing
~ find tree center

1: root similarly
2: encode trees (brackets, or 0-es 1-es)
3: compare

AHU algo for serialization
- leaf nodes = Knuth tuples ()
- wrap children with Knuth tuples
- child labels need sorting when combined
"""
from tree_center import tree_center
from rooting_tree import root_tree

def tree_isomorphic(tree1, tree2):
    #check if trees are empty

    #find centers
    centers1 = tree_center(tree1)
    centers2 = tree_center(tree2)

    #serialize trees
    rooted1 = root_tree(tree1, centers1[0])
    encoded1 = encode(rooted1)

    for center in centers2:
        rooted2 = root_tree(tree2, center)
        encoded2 = encode(rooted2)
        if encoded1 == encoded2:
            return True
    
    return False

def encode(node):
    #pass in root first

    #base case
    if node == None:
        return ""
    
    labels = LinkedList()

    for child in node.children():
        labels.add(encode(child))
        labels = sorted(labels)
    
    str1 = ""

    for label in labels:
        str1 += label
    
    return "("+str1+")"








class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)
        