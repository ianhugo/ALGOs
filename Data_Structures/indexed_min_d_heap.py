def compareTo(num1, num2):
    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1

#ki = key index, assigned to each node

class D_Heap:
    def __init__(self, degree, max_nodes):
        self.heap = []
        self.node_map = {}
        self.degree = None
        self.capacity = None
        self.sz = None

        self.child = []
        self.parent = []

        self.index_value = {}
        self.value_index = {}

        self.values = []        #key index: value
        self.position = []     #key index: position index in heap
        self.inverse = []       #position index in heap: key index
        self.initialize(degree, max_nodes)
        pass

    def initialize(self, degree, max_nodes):
        self.degree = max(2, degree)
        self.capacity = max(degree + 1, max_nodes)


        for i in range(self.capacity):
            self.parent[i] = (i-1)/ self.degree
            self.child[i] = i * self.degree + 1
            self.positions[i] = self.inverse[i] = -1
    
    def less(self, index1, index2):
        node1 = self.values[self.inverse[index1]]
        node2 = self.values[self.inverse[index2]]
        return (compareTo(node1, node2) <= 0)

    def isEmpty(self):
        return (self.size()==0)
    
    def size(self):
        return self.sz
    
    def contains(self, ki):
        self.key_inbounds(ki)
        return self.position[ki] != -1
    
    def peek_min_ki(self):
        return self.inverse[0]
    
    def poll_min_ki(self):
        min_ki = self.peek_min_ki()
        self.delete(min_ki)
        return min_ki
    
    def peek_min_ki_val(self):
        min_ki = self.peek_min_ki()
        return self.values[self.inverse[min_ki]]
    
    def poll_min_val(self):
        min_val = self.peek_min_ki_val()
        self.delete(self.peek_min_ki())
        return min_val
    
    def insert(self, ki, value):
        if self.contains(ki):
            print("Index already exists")
            return
        
        self.value_null(value)

        self.position[ki] = self.sz
        self.inverse[self.sz] = ki
        self.values[ki] = value
        self.swim(self.sz)
        self.sz += 1

    def get_val(self, ki):
        self.key_exist(ki)
        return self.values[ki]
    
    def delete(self, ki):
        self.key_exists(ki)
        pos = self.position[ki]
        self.swap(pos, self.sz)
        self.sz -= 1

        self.sink(pos)
        self.swim(pos)

        value = self.values[ki]
        self.position[ki] = -1
        self.inverse[ki] = -1

        return value
    
    def update(self, ki, val):
        self.key_exist_val_good(ki, val)
        pos = self.position[ki]
        old = self.values[ki]
        self.values[ki] = val
        self.sink(pos)
        self.swim(pos)
        return old
    
    def decrease(self, ki, val):
        self.key_exist_val_good(ki, val)
        if self.less(val, self.values[ki]):
            self.values[ki] = val
            self.swim(self.position[ki])
    
    def increase(self, ki, val):
        self.key_exist_val_good(ki, val)
        if self.less(val, self.values[ki]):
            self.values[ki] = val
            self.sink(self.position[ki])

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

    def swap(self, pos1, pos2):
        self.position[self.inverse[pos2]] = pos1
        self.position[self.inverse[pos1]] = pos2
        self.inverse[pos1], self.inverse[pos2] = self.inverse[pos2], self.inverse[pos1]
    
    def key_inbounds(self, ki):
       if ki<0 or ki >= self.capacity:
            print("Key out of bounds")
    
    def value_null(self, val):
        if val == None:
            print("Bad value")

    def key_exists(self, ki):
        if not self.contains(ki):
            print("Key Index does not exist")

    def key_exist_val_good(self, ki, val):
        self.key_exists(ki)
        self.value_null(val)
        pass

