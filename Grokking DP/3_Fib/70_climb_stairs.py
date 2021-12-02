"""
Given: n steps
Want: method, count possible ways to reach top of stairs
Each step [1, 2, 3]


BRUTE:
- count every combination
- reach 0, return 1
- recurse back, combinig

at this step, step 1
at this step, step 2
at this step, step 3

"""


"""BRUTE"""

def count_brute(n):
    #no more steps needed
    #reached the end
    if n == 0:
        return 1
    
    #one more step needed
    if n ==1:
        return 1
    
    #two more steps needed
    if n ==2:
        return 2    #1+1 or 2
    
    #only these 2, because all numbers odd or even

    step1 = count_brute(n-1)
    step2 = count_brute(n-2) 
    step3 = count_brute(n-3)

    return step1 + step2 + step3

"""Top-Down"""

def solve(n):
    dp = [0 for _ in range(n+1)]    #n+1 as need base case
    dp = count(dp, n)
    return dp[-1]

def count(dp, n):

    if n ==0:
        return 1
    
    if n ==1:
        return 1
    
    if n==2:
        return 2

    if dp[n] == 0:
        step1 = count(dp, n-1)
        step2 = count(dp, n-2) 
        step3 = count(dp, n-3)
        dp[n] = step1 + step2 + step3
    
    return dp[n]

"""Bottom-up"""
def count_ways(n):
  dp = [0 for x in range(n+1)]
  dp[0] = 1
  dp[1] = 1
  dp[2] = 2

  for i in range(3, n+1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

  return dp[n]