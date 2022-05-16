'''
Given a binary tree and two nodes in that tree, find the lowest common ancestor of those nodes.
//     3
//    / \
//   9   7
//  / \   \
// 2   6   4

// 2, 6 -> 9
// 7, 6 -> 3

// 3, 7 ->3
'''

class lca_solver:
    
    def __init__(self, root, node1, node2):
        self.root = root
        self.node1 = node1
        self.node2 = node2
        self.lca = None
        self.lca_solved = False
        self.node1_found = False
        self.node2_found = False
    
    def solve(self):
        self.recurse(self.root)
        return self.lca_solved, self.lca
        
        
    def recurse(self, curr_node):

        if not curr_node:
            return False
        
        mid = None
        if curr_node == self.node1 and not self.node1_found:
            self.node1_found = True
            mid = True
            # return True
        
        if curr_node == self.node2 and not self.node2_found:
            self.node2_found = True
            mid = True
            # return True

        left = recurse(curr_node.left)

        right = recurse(curr_node.right)
        
        if (mid and left) or (mid and right) or (left and right):
            self.lca = curr_node
            self.lca_solved = True
        
        return left or right

def main():
    solver = lca_solver(root, node1, node2)
    bool_res, lca = solver.solve()  
    
    
'''
Plan a round trip between two cities with minimum flight cost.

From departure city to destination city, the direct flight fee is stored in array D[].
From destination city to departure city, the direct flight fee is stored in array R[].

D: [10, 8, 9, 11, 7]
R: [8,  8, 10, 7, 9]

The minimum cost will be D[1] + R[3] = 15

1: want minimum cost of D[i] + R[j]
2: i <= j
'''

import math

def opt_solve(D, R):
    d_len = len(D)
    r_len = len(R)
    pre_arr = [0]*r_len
    curr_r_min = math.inf
    
    #precompute running min
    for i in range(r_len, 0, -1):
        if R[i] < curr_r_min:
            curr_r_min = R[i]
        pre_arr[i] = curr_r_min
    
    running_min = math.inf
    
    for j in range(d_len)
        curr_min = D[j] + pre_arr[j]
        if curr_min < running_Min:
            running_Min = curr_min
    
    return running_min
    

# def solve(D, R):
    
#     d_len = len(D)
#     r_len = len(R)
#     d_min = math.inf
#     r_min = math.inf
    
    
#     for i in range(d_len):
#         if D[i] < d_min:
#             d_min = D[i]
    
#     for i in range(r_len):
#         if R[i] < r_min:
#             r_min = R[i]
    
#     return d_min

def brute_solve(D, R):
    """
    O(n^2)
    """
    
    d_len = len(D)
    r_len = len(R)
    curr_min = math.inf
    
    for i in range(d_len):    #O(n) n = d_len
        for j in range(i, r_len):    #O(m) m = r_len
            curr_sum = D[i] + R[j]
            if curr_sum < curr_min:
                curr_min = curr_sum
    
    return curr_min


            
    














###################################


# Description
# Given an array of integers, find any one local minimum from the array. A local minimum is defined as an integer in the array that is less than or equal to its neighbors.

# [5, 9, 7, 10, 12]


"""
GIVEN: array of ints
WANT: a local minimum
- arr[i] <= arr[i-1] and arr[i]<= arr[i+1]


"""

def local_min(arr):
    
    res = None
    n = len(arr)
    
    for i in range(0, n):
        
        if i == 0:
            if arr[0] <= arr[1]:
                return res
        if i== (n-1)
            if arr[-1] <= arr[-2]:
                return res
        
        if arr[i] <= arr[i-1] and arr[i]<= arr[i+1]:
            res = arr[i]
            return res
        
    
    return res


def local_min_recur(arr, low, high, n):  #[5, 9, 7, 10, 12]          #[5, 9, 10, 11, 12]
    
    mid = low + (high - low)//2
    
    #edge case
    if (mid == 0 and arr[mid] <= arr[mid+1]) or (mid == n-1 and arr[mid] <= arr[mid-1]):
        return mid
    #check
    elif(arr[mid-1] >= arr[mid] and arr[mid+1] >= arr[mid]):
        return mid
    #right halve
    elif (arr[mid+1] <= arr[mid])
        return local_min_recur(arr, mid+1, high, n)
    #left halve
    else:    #arr[mid-1] < arr[mid]
        return local_min_recur(arr, low, mid-1, n)        #low = 0, 1
    
    
    
    

    

    
#     Description
# Given an integer array and an integer number k. Return the k-th largest element in the array.

# Examples:
# array = [5, -3, 9, 1]
# * k = 0 => return: 9
# * k = 1 => return: 5
# * k = 3 => return: -3


"""
Given: int array, k
WANT: the k-th largest, sorted ascneding k-th

NAIVE: sort -> n lg n, sorted[k]

heap

"""


import heapq

def find_kth(arr, k):
    
    #maintain heap of size k
    #heap.pop()
    #heap.add()
    
    n = len(arr)
    heap = heapq() #default min
    
    for i in range(n):        #O(n)
        if arr[i] >= heap[0]:    #O(lg k)
            heap.add(arr[i])    #heapifies
            while len(heap) > (k+1):
                heap.pop()    #heapifies
    
    return heap[0]
        
        
    [-3, -3, -3, -3] [5, -3, -3, 9]
    
    #[5, -3, -3, 9], k= 2
    
    


    