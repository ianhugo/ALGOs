"""
Given: k sorted array
Want: sorted traversal

General Approach:

1. Basic
- iterate through each array, one at a time
- insert each into a heap
- mark them with heap id
- then pop one off at a time
- then pop from appropriate heap back

NOTE: at any point, the heap has size k (number of lists)

2. Finding Best Ranges
- iteratively push
- keep track of current max
- keep track of running min


"""