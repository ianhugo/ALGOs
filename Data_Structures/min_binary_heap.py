"""implementation of binary heap

This is a MIN heap
for MAX heap
OPTION 1: reverse sink/swim logic
OPTION 2: negate values then put in, negate values when pull out

for numeric/comparable data in array
"""

def compareTo(num1, num2):
    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1

class Binary_Heap:
    def __init__(self):
        self.heap = []
        self.node_map = {}
        pass
    
    def size(self):
        return len(self.heap)
    
    def less(self, index1, index2):
        node1 = self.heap[index1]
        node2 = self.heap[index2]
        return (compareTo(node1, node2) <= 0)

    def swap(self, index1, index2):
        elem1 = self.heap[index1]
        elem2 = self.heap[index2]
        elem1, elem2 = elem2, elem1
        self.mapSwap(elem1, elem2, index1, index2)  #QUICK REMOVALs

    def isEmpty(self):
        return (self.size()==0)
    
    def clear(self):
        self.heap = []

    def peek(self):
        if self.isEmpty():
            return None
        else:
            elem = self.heap[0]
            return elem
    
    def poll(self):
        return self.removeAt(0)
    
    def add(self, value):
        if value == None:
            return None
        
        self.heap.append(value)
        last_index = self.heap.size() -1
        self.mapAdd(value, last_index) #QUICK REMOVALS
        self.swim(last_index)
    
    def addAll(self, arr): #O(n)

        heapSize = len(arr)
        # for i in range(0, heapSize, 1):
        #    self.add(arr[i])
        for j in range(len(arr)):
            self.mapAdd(arr[j], j)  #QUICK REMOVALS
            self.heap.append(arr[j])

        for i in range(max(0, (heapSize/2)-1), 0, -1):
            self.sink(i)
    
    def remove(self, target_value):
        
        if target_value == None:
            return False
        
        #O(n) slow version
        for i in range(len(self.heap)):         #searching all
            if target_value == self.heap[i]:
                self.removeAt(i)
                return True
        
        #QUICK REMOVALS
        #O(lg n) removals
        # index = self.mapGet(target_value)
        # if index != None:
        #     self.removeAt(index)
        #     return True

        return False

    def removeAt(self, target):
        """remove and heapify
        O(lg n)"""
        if self.isEmpty():
            return None
        
        last_index = self.size() - 1
        removed_data = self.heap[target]
        self.swap(target, last_index)

        self.heap.pop[last_index]
        self.mapRemove(removed_data, last_index)

        if (target == last_index):
            return removed_data
        
        elem = self.heap[target]
        
        self.sink(target)

        if self.heap[target] == elem:
            self.swim(target)
        
        return removed_data

    def sink(self, target): #O(lg n)
        heapSize = self.size()

        while True:
            left = 2 * target + 1    #child index
            right = 2 * target + 2
            smaller = left
            
            #checking if smaller is indeed left child
            if (right < heapSize and self.less(right, left)):
                smaller = right
            
            #stopping early
            # 1: out of bounds
            # 2: cannot sink index anymore
            if (left >= heapSize or self.less(target, smaller)):
                break

            self.swap(target, smaller)
            target = smaller

        pass

    def swim(self, arr, target): #O(lg n)
        
        parent = (target -1)/2

        while (target > 0 and self.less(target, parent)):
            self.swap(target, parent)
            target = parent
            parent = (target-1)/2

        pass
    

    #QUICK REMOVAL utility functions

    def mapAdd(self, value, pos):
        try:
            self.node_map[value].append(pos)
        except:
            self.node_map[value] = [pos]
        pass

    def mapRemove(self, value, pos):
        set1 = self.node_map[value]

        #implement as hash of hash? or BST?
        for i in range(len(set1)):
            if set1[i] == pos:
                set1 = set1.pop(i)
                break
        
        if len(set1) == 0:
            removed_value = self.node_map.pop(value, 'No Key found')
        else:
            self.node_map[value] = set1
        pass

    def mapSwap(self, val1, val2, pos1, pos2):

        set1 = self.node_map[val1]
        set2 = self.node_Map[val2]

        #swap them 
        #this is inefficient, might be better to use indexed version
        pass

    def mapGet(self, value):
        arr1 = self.node_map[value]
        if arr1 != None:
            pos = arr1.pop(-1)
            return pos
