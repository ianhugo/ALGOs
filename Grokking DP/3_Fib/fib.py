"""Brute"""

def fib_brute(n):
    if n<2:
        return n
    
    return fib_brute(n-1) + fib_brute(n-2)

"""Top-Down Memoize"""

def fib(n):
    memo = [-1 for x in range(n+1)]
    return fib_recur(memo, n)

def fib_recur(memo, n):
    if n<2:
        return n
    
    if memo[n] >= 0:   #calcualted
        return memo[n]
    memo[n] = fib_recur(memo, n-1) + fib_recur(memo, n-2)

    return memo[n]

"""Borrom-Up Tab"""

def fib2(n):
    if n< 2:
        return n
    
    dp = [0, 1]

    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    
    return dp[n]

"""Optimize Space
only need two previous"""

def calculateFibonacci(n):
  if n < 2:
    return n

  n1, n2, temp = 0, 1, 0
  for i in range(2, n + 1):
    temp = n1 + n2
    n1 = n2
    n2 = temp

  return n2
