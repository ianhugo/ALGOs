

class Node:
    def __init__(self, val):
        self.val = val
        self.index = None
        self.priority = None
        self.parent = None
        self.left = None
        self.right = None
        self.height = None
        self.bf = None
        pass

class NodeHash:
    def __init__(self):
        self.dict_node = {}