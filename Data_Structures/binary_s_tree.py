"""

Traversals

Inorder: left, root, right
Preorder: Root, left, right
Postorder: left, right, root
Vread-First or level Order Traversal: increasing sequence

"""


class BST():
	def __init__(self):
		self.count = 0
		self.root = None
	
	def contains_public(self, data):
		return self.contains_private(self.root, data)

	def contains_private(self, node, data):
		if node == None:	#base case, leaf
			return False
		cmp = node.compareTo(data)

		if cmp <0:
			return self.contains_private(node.left, data)
		elif (cmp > 0):
			return self.contains_private(node.right, data)
		else:
			return True

	def add_public(self, data):
		if self.contains_public(data):
			return False
		else:
			root = self.add_private(self.root, data)
			self.count += 1
			return True
	
	def add_private(self, node, data):
		if node == None:	#base case, create root/leaf_node
			node = Node(None, None, data)
		else:
			if node.compareTo(data) < 0:
				node.left = self.add_private(node.left, data)
			else:
				node.right = self.add_private(node.right, data)

		return node
        
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
			self.count -= 1
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
				tmp = self.find_min(node.right)
				node.data = tmp.data
				node.right = self.remove_private(node.right, tmp.data)
		return node

	def height_public(self):
		return self.height_private(self.root)
	
	def height_private(self, node):
		if node == None:
			return 0
		return max(self.height_private(node.left), self.height_private(node.right)) + 1

	#traversals

class Node:
	def __init__(self, left, right, data):
		self.data = data
		self.left = left
		self.right = right

	def compareTo(self, data):
		if self.data < data:
			return 1
		elif self.data > data:
			return -1
		else:
			return 0