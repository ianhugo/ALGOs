"""
Given: set of elements
Want: all distinct subsets

Thoughts:
model as a tree
nodes = elements
choose one as root
do carryover BFS

Idea:
1. start with empty set
2. node =  result
3: left child/children = copied from last level
4: right child/children = add new element to each

"""

"""
O(n*2^n)

O(n*2^n) space
"""

def find_subset(nums):
    subsets = []

    subsets.append([])

    for curr in nums:   #element to add on each layer
        n = len(subsets)

        #for each new number
        #append to all curreent subsets
        #append this new version to overall result
        for i in range(n):  #current level how long
            set1 = list(subsets[i]) #add to each subset
            set1.append(curr)
            subsets.append(set1)    #append new