"""
Given: denoms, total
Want: minimum number of coins, to make up amount

Idea:
- same as count all
- but instead of incrementing at each step
- take cardinality, take min
"""

"""
Top-Down
"""

import math

def count(denom, total):
    dp = [[-1 for _ in range(total+1)] for _ in range(len(denom))]
    result = count_recur(dp, denom, total, 0)
    return -1 if result == math.inf else result

def count_recur(dp, denom, total, curr_idx):

    if total == 0:
        return 0
    
    n = len(denom)

    if n == 0 or curr_idx >= n:
        return math.inf
    
    if dp[curr_idx][total] == -1:
        count1 = math.inf

        #include
        if denom[curr_idx] <= total:
            res = count_recur(dp, denom, total - denom[curr_idx], curr_idx)
        
            if res != math.inf:
                count1 = res +1
        
        #exclude
        count2 = count_recur(dp, denom, total, curr_idx +1)

        dp[curr_idx][total] = min(count1, count2)

    return dp[curr_idx][total]

"""Bottom-up"""

def count2(denom, total):
    n = len(denom)

    dp = [[math.inf for _ in range(total+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0
    
    for i in range(n):
        for t in range(1, total+1):
            if i>0:
                dp[i][t] = dp[i-1][t]
            
            if t>= denom[i]:
                #include, last position has solution
                last = dp[i][t-denom[i]]
                if last != math.inf:
                    dp[i][t] = min(dp[i][t], last + 1)
    
    return -1 if dp[n-1][total] == math.inf else dp[n-1][total]
    