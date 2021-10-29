
def compareTo(num1, num2):
    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1

class D_Heap:
    def __init__(self, degree, max_nodes):
        self.heap = []
        self.node_map = {}
        self.degree = None
        self.capacity = None
        self.child = []
        self.parent = []
        self.sz = None
        self.initialize(degree, max_nodes)
        pass
    
    def size(self):
        return self.sz
    
    def less(self, index1, index2):
        node1 = self.heap[index1]
        node2 = self.heap[index2]
        return (compareTo(node1, node2) <= 0)

    def swap(self, index1, index2):
        elem1 = self.heap[index1]
        elem2 = self.heap[index2]
        elem1, elem2 = elem2, elem1

    def isEmpty(self):
        return (self.size()==0)
    
    def clear(self):
        self.heap = [None] * self.capacity
        self.sz = 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            elem = self.heap[0]
            return elem
    
    def poll(self):
        pass

    def initialize(self, degree, max_nodes):
        self.degree = max(2, degree)
        self.capacity = max(degree, max_nodes)


        for i in range(self.capacity):
            self.parent[i] = (i-1)/ self.degree
            self.child[i] = i * self.degree + 1
    
    def add(self, value):
        if value == None:
            return None
        
        self.heap[self.sz] = value
        self.swim(self.sz)
        self.sz += 1

    def poll(self):
        if self.isEmpty():
            return None
        
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = None
        self.sink(0)
        return root
    

    def sink(self, index):

        tmp = self.minChild(index)

        while tmp != -1:
            self.swap(index, tmp)
            index = tmp
            tmp = self.minChild(index)

        pass

    def swim(self, index):
        while self.less(index, self.parent[index]):
            self.swap(index, self.parent[index])
            index = self.parent[index]
        pass

    def minChild(self, index):
        track = -1
        start = self.child[index]
        end = min(self.sz, start + self.degree)

        for i in range(start, end):
            if self.less(i, index):
                track = i
                index = i
        
        return index
