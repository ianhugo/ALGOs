"""
Given: array of ints, k
(can have negative)

WANT: total number of continuous subarrays
sum equal to k

IDEA:
- increment, whenever sums has increased by value of k
"""


"""PREFIX SUM idea
- calcualte prefix sum array
- pre_sum[i] = pre_sum[i-1]+ arr[i]
- sum for nums[i:j] = sums[j+1]- sums[i]
- then try all combinations

WHY PREFIX SUM:
- can calculate intervals more quickly, O(1)
- only need to calculate through 1 time


"""

"""FASTEST"""

def sum3(nums, k):
    count = {}
    csum = 0
    res = 0

    for n in nums:

        csum += n       #add on each time
        if csum ==k:    #if matched then increment, first time
            res += 1
        if csum-k in count: #subsequent times, if can go back to previous
            res += count[csum-k]    #how many previous
        
        if csum in count:   #2 subarrays with this sum
            count[csum]+=1
        else:   #1 subarray with this sum
            count[csum] = 1
    
    return res