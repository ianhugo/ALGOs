"""
Given: unsorted array, target number
Want: 4 unique, sum to target

BRUTE:

- sort it
- three way sum
- binary search
"""

##question: how does this cover all permutations?

"""
#####Iteration

O(n^3) = three loops
last loop at most goes all n

O( n lg n) = sorting
"""
def search_quad(arr, target):
    arr.sort()
    quads = []
    for i in range(0, len(arr)-3): #overlaps
        if i> 0 and arr[i] == arr[i-1]: #skip dups
            continue

        #for each two consecutive, choose
        for j in range(i+1, len(arr)-2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            search_pairs(arr, target, i, j, quads)
    
    return quads

def search_pairs(arr, target, first, second, quads):
    left = second +1
    right = len(arr)-1

    while left < right:
        quadsum = arr[first] + arr[second] + arr[left] + arr[right]
        if quadsum == target:
            quads.append(arr[first], arr[second], arr[left], arr[right])
            left += 1
            right -= 1

            #skip dups
            while (left < right and arr[left] == arr[left-1]):
                left += 1
            while (left< right and arr[right] == arr[right+1]):
                right -= 1
        
        #change next considerations
        elif quadsum < target:
            left += 1
        else:
            right -=1


"""
#####Recursive

O(n^3) = three loops
last loop at most goes all n

O( n lg n) = sorting


NOTE:understanding Recursion
set base cases, conditions to check
think about in branches
at each branch, how to divide subproblems
can solve upwards
same kind of solution
then when come up, how to combine
"""

def ksum(arr, target, k):
    """
    k = number of elements wanted

    O(n^(k-1)) time
    k-2 loops
    twoSum = O(n)
    """

    res = []

    if not arr: #if empty, truth val of python
        return res
    
    #floor division
    #use to stop early
    avg_val = target //k

    #if smallest value in arr > target
    #if largest value in arr < target
    #both can stop early
    if avg_val < arr[0] or arr[-1] < avg_val:
        return res
    
    #if choose enough elements, only two left
    if k==2:
        return two_sum(arr, target)
    
    for i in range(len(arr)):
        #skip dups
        if i==0 or arr[i-1] != arr[i]:

            #pass in smaller array
            #smaller sum
            #smalle number of k
            for subset in ksum(arr[i+1:], \
                target - arr[i], k-1):
                #rnew results
                res.append(arr[i]+subset)
    return res

def two_sum(arr, target):
    res = []
    lo, hi = 0, len(arr)-1

    while lo<hi:
        curr_sum = arr[lo] + arr[hi]

        #if too small, or have dups
        if curr_sum < target or \
            (lo > 0 and arr[lo] == arr[lo-1]):
            lo +=1
        
        #if too big, or have dups, not at start
        elif curr_sum > target or\
            (hi < len(arr)-1 and arr[hi] == arr[hi+1]):
            hi -=1
        
        else:   #equal to target
            res.append(arr[lo], arr[hi])
            lo += 1
            hi -=1
    return res



