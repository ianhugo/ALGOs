
#array based

from collections import deque
#c-based implementation, with O(1) operaitons

max_size = 0
elem = 1
queue = deque(maxlen = max_size)

#append right
queue.append(elem)

#append left
queue.appendleft(elem)

#clear
queue.clear()

#count elem(s)
count_of_elem = queue.count(elem)

#index of elem, start stop, positions are each optional
idx = queue.index(elem, 0, 1)

#insert
position = 2
queue.insert(position, elem)

#pop from right
right_end = queue.pop()

#pop from left
left_end = queue.popleft()

#remove (first occur)
queue.remove(elem)

queue.reverse()



#####LINKED LIST
class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.length += 1

    def dequeue(self):
        item = self.head.item
        self.head = self.head.next 
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item


class Queue1:
    def __init__(self, length):
        """a queue of at most n elements using an array of n+1 element size"""
        self.length = length
        self.queue = [None]*(length+1)
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if self.is_full():
            return 'Overflow'
        self.queue[self.tail] = x
        if self.tail == self.length:
            self.tail = 0
        else:
            self.tail = self.tail + 1

    def dequeue(self):
        if self.is_empty():
            return 'Underflow'
        x = self.queue[self.head]
        if self.head == self.length:
            self.head = 0
        else:
            self.head = self.head + 1
        return x

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def is_full(self):
        if self.head == self.tail+1 or (self.head == 0 and self.tail == self.length):
            return True
        return False