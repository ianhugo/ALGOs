"""
GIven: BST
WANT: doubly linked list

O(n)
"""

class Solver:
    def __init__(self, root):
        self.root = root
        self.last = None
        self.first = None
    
    def solve(self):
        self.recur(self.root)

        #link first and last, close linked list
        self.last.right = self.first
        self.first.left = self.last

        return self.first
    
    def recur(self, node):  #inorder traversal (left -> node -> right) -> up
        if node:
            self.recur(node.left)

            if self.last:
                self.last.right = node
                self.node.left = self.last
            else:
                self.first = node
            
            self.last = node

            self.recur(node.right)
