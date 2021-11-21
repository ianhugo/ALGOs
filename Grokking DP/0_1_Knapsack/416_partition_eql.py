"""
Given: set of positive integers
Want: bool, partition intwo 2 subsets
= sum of elements in both is equal

Idea:
- choose certain numbers
- constraint: only n/2 numbers
- optimzie: sum = sum left

- target = sum of all/2

Brute:
- generate all permutations
- calcualte for all

Bottom-up:
- reminds of 0/1 knapsack
- at each point choose or not choose this number
- have this much target left
- capacity = target

- n x c table
- pad values first
- for i in range(n):
    for c in range(target):

        #include
            #decrement cap
            #go up one row
        #exclude
            #go up one row
        
        #take maximum

Easier with Recursion:
- pass down target

def knap_recur(arr, remain, target, curr_idx):

    if remain <0 or (out of bounds):
        return False
    
    if (remain - arr[curr_idx]) == 0:
        res.append(curr_idx)
        return True, res

    #include
    included, res1 = knap_recur(arr, (remain-arr[curr_idx]), target, (curr_idx-1))
    if included:
        res1.append(curr_idx)
        return True, res1

    #exclude
    excluded, res2 = knap_recur(arr, remain, target, curr_idx-1)
    if excluded:
        return True, res2
    
    return False

OPTIMIZE with DP
- overlapping, with this much left, whether include this number
- dp_table = n x target
- initialize with -1
- cache: (included_bool)
    - None if dead-end
- check: included_bool?

"""

def can_partition(num):
    s = sum(num)

    if s%2 != 0:
        return False
    
    dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]

    return True if recur(dp, num, int(s/2), 0) ==1 else False

def recur(dp, num, sum, curr_idx):

    #found
    if sum == 0:
        return 1
    
    #validation
    n = len(num)
    if n ==0 or curr_idx >= n:
        return 0
    
    #processed?
    if dp[curr_idx][sum] == -1:
        
        #possible?
        if num[curr_idx] <= sum:
            if recur(dp, num, sum - num[curr_idx], curr_idx +1) ==1:
                dp[curr_idx][sum] = 1
                return 1
            
        dp[curr_idx][sum] = recur(dp, num, sum, curr_idx+1)
    
    return dp[curr_idx][sum]