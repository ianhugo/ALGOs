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

-----------------------
2. Finding Best Ranges (smallest range)
- iteratively push from each list
- keep track of current max in the heap
- pop the min
- keep track of the best range

-----------------------
3. K Largest Pairs
- double loop
- maintain k-sized heap
- add (arr[i]+arr[j], i, j) into heap
- compare to top, if the sum is smaller
- then break, as everything after will be smaller


"""