"""
Given: int array, might have duplicates
Want: all possible subsets

use additional space to have a hash set of elements went over

ISSUE: will skip over double 3 patterns

RESOLVE: only add a duplicate to the half of subsets array
so don't do first half
"""

def find_subsets(nums):

    list.sort(nums)
    subset = []
    subset.append([]) #first empty
    start, end = 0, 0

    #loop over all
    for i in range(len(nums)):
        start = 0

        #if not first, and duplciate
        if i>0 and nums[i] == nums[i-1]:
            start = end +1
            #this end has not been updated
            #make the start the previous end

        end = len(subset) -1

        #do regular operation
        for j in range(start, end +1):
            set1 = list(subset[j])
            set1.append(nums[i])
            subset.append(set1)
    
    return subset