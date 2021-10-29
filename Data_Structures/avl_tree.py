from node import Node

def compareTo(num1, num2):
    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1


class AVL_Tree:
    def __init__(self):
        self.root = None
        self.node_count = None
    
    def height(self):
        if self.root == None:
            return 0
        return self.root.height
    
    def isEmpty(self):
        return self.node_count == 0

    def contains(self, val):
        return self.contains_prv(self.root, val)

    def contains_prv(self, node, val):
        if node == None:
            return False
        
        cmp = compareTo(val, node.val)

        if cmp <0: 
            return self.contains(node.left, val)
        elif cmp >0:
            return self.contains(node.right, val)
        else:
            return True
    
    def insert(self, val):
        if val == None:
            return False
        elif not self.contains(self.root, val):
            self.root = self.insert_prv(self.root, val)
            self.node_count += 1
            return True
        else:
            return False
    
    def insert_prv(self, node, val):
        if node == None:
            new = Node()
            new.val = val
            return new
        
        cmp = compareTo(val, node.val)

        if cmp < 0:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        
        self.update(node)
        return self.balance(node)
    
    def update(self, node):
        if node.left == None:
            left_height = -1
        else:
            left_height = node.left.height
        
        if node.right == None:
            right_height = -1
        else:
            right_height = node.right.height
        
        node.height = max(left_height, right_height)

        node.bf = right_height - left_height
    
    def balance(self, node):

        if node.bf == -2:
            if node.left.bf <= 0:   
                return self.left_left_case(node)
            else:
                return self.left_right_case(node)
        elif node.bf == 2:
            if node.right.bf >= 0:
                return self.right_right_case(node)
            else:
                return self.right_left_case(node)
        else:
            return node
    
    def left_left_case(self, node):
        return self.right_rotate(node)

    def left_right_case(self, node):
        node.left = self.left_rotate(node.left)
        return self.left_left_case(node)
    
    def right_right_case(self, node):
        return self.left_rotate(node)
    
    def right_left_case(self, node):
        node.right = self.right_rotate(node.right)
        return self.right_right_case(node)
    
    def left_rotate(self, node):

        new_par = node.right
        node.right = new_par.left
        new_par.left = node
        self.update(node)
        self.update(new_par)
        return new_par

    def right_rotate(self, node):
        new_par = node.left
        node.left = new_par.right
        new_par.right = node
        self.update(node)
        self.update(new_par)
        return new_par
    
    def find_min(self, node):
        while(node.left != None):
            node = node.left
            return node
    def find_max(self, node):
        while (node.right != None):
            node = node.right
        return node
    
    def remove_public(self, data):
        if self.contains(data):
            self.root = self.remove_private(self.root, data)
            self.node_count -= 1
            return True
        else:
            return False
    
    def remove_private(self, node, data):
        if node == None:
            return None
        cmp = node.comapre(data)
        if cmp < 0:		#recursing down
            node.left = self.remove_private(node.left, data)
        elif cmp > 0:
            node.right = self.remove_private(node.right, data)
        else:		#found
            if node.left == None: #one sided 
                return node.right
            elif node.right == None:
                return node.left	
            else:	#two subtrees
                if node.left.height > node.right.height:    #remove from left
                    successor = self.find_max(node.left)
                    node.val = successor
                    node.left = self.remove_private(node.left, successor)
                else:
                    successor = self.find_min(node.right)
                    node.val = successor
                    node.right = self.remove_private(node.right, successor)

        self.update(node)
        return self.balance(node)

