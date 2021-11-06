"""
tree-like structure
root and children

split up a sequence into layers of trees, each layer with Bool
C - A - R
C = root, F
A = node, F
R = node, F
null = leaf, T
can add cat to this, now A will ahve a child T

https://www.youtube.com/watch?v=-urNrIAQnNo
"""

class Trie_Node:
    def __init__(self, ch):
        self.char = ch
        self.count = 0
        self.ending = False
        self.children = {}
    
    #provide character of child, and node of child
    def add_child(self, ch, node):
        self.children[ch] = node

class Trie:
    def __init__(self):
        self.root = Trie_Node(None)
    
    def insert(self, key, num_inserts=1):
        #return True if string contains prefix 

        node = self.root
        created_node = False
        is_prefix = False

        length = len(key)
        for i in range(length): #process one char at a time
            ch = key[i]
            if ch not in node.children: #does not exist yet
                next_node = Trie_Node(ch)
                created_node = True
            else:   #does exist
                next_node = node.children[ch]
                if next_node.ending:
                    is_prefix = True
        
            node = next_node
            node.count += num_inserts
        
        if node != self.root:
            node.ending = True
        
        return is_prefix or (not created_node)

    def delete(self, key, num_delete = 1):

        if not self.contains(key):
            return False
        
        length = len(key)
        node = self.root
        for i in range(length):
            ch = key[i]
            cur_node = node.children[ch]
            cur_node.count -= num_delete

            if cur_node.count <= 0:
                del node.children[ch]
                cur_node.children = None
                cur_node = None
                return True
            
            node = cur_node
        
        return True
        

    def contains(self, key):
        return self.count(key) != 0

    def count(self, key):
        #count of a particular prefix

        node = self.root

        #dig into trie
        #until reach bottom or stop early
        for i in range(len(key)):
            ch = key[i]
            if ch not in node.children: 
                return 0
            else:
                node = node.children[ch]
        
        if node != None:
            return node.count
        
        return 0

                



