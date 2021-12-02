"""
Given: rod of length n, price of lengths
Want: maximize chopped up profit

IDEA:
- unbounded knapsack
- capacity constraint is n
- each row = rod of length i
- each column = remaining capacity


"""


def solve(lengths, price, n):
    lent = len(lengths)

    if n <= 0 or lent == 0 or len(price) != lent:
        return 0
    
    dp = [[0 for _ in range(n+1)]for _ in range(lent)]

    for i in range(lent):   #all possible lengths
        for length in range(1, n+1):    # all constraint lengths
            p1, p2 = 0, 0

            if lengths[i] <= length:    #if less than constraint length
                p1 = price[i] + dp[i][length - lengths[i]]
            if i>0:
                p2 = dp[i-1][length]
            
            dp[i][length] = max(p1, p2)
    
    #return bottom-right
    return dp[length-1][n]
