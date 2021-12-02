"""
Given: infinite n coin demoninations, total amount x
Want: total ways to make change


IDEA:
- unbounded knapsack
- rows = type of coin
- columns = increasing number to target
- don't maximize, just count number of ways
"""


"""Top-down"""
def coin_change(denom, total):
    dp = [[-1 for _ in range(total+1)] for _ in range(len(denom))]
    return coin_recur(dp, denom, total, 0)

def coin_recur(dp, denom, total, curr_idx):
    
    if total == 0:
        return 1
    
    n = len(denom)

    if n == 0 or curr_idx >= n:
        return 0
    
    if dp[curr_idx][total] != -1:
        return dp[curr_idx][total]
    
    sum1 = 0

    #include, this, permutations
    if denom[curr_idx] <= total:
        sum1 = coin_recur(dp, denom, total - denom[curr_idx], curr_idx)
    
    sum2 = coin_recur(dp, denom, total, curr_idx+1)

    dp[curr_idx][total] = sum1 + sum2

    return dp[curr_idx][total]

"""Bottom-up"""

def count(denom, total):
    n = len(denom)

    dp = [[0 for _ in range(total+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1
    
    for i in range(n):
        for t in range(1, total+1):
            if i>0:
                dp[i][t] = dp[i-1][t]   #exclude
            if t >= denom[i]:   #include
                dp[i][t] += dp[i][t-denom[i]]
    
    return dp[n-1][total]
    