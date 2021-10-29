
"""
heapsort
1. pass arrary in
2. make into a min heap
3. dequeue one by one
4. add to new array
"""

from Data_Structures import min_binary_heap

def heapsort(arr):
    heap = min_binary_heap.Binary_Heap()   #min heap, negate values for max heap
    heap.addAll(arr)

    sorted = []
    for i in range(len(arr)):
        elem = heap.poll()
        sorted.append(elem)
    
    return sorted