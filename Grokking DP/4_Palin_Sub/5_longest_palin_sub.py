"""

Substring, means no deletion

have to match all the way

BRUTE:
choose each as middle
expand out

Top-down:
keep track of start and end

BRUTE:
Check if the same, if so, call smaller
If not, then call smaller on each side
return: if valid, return the pair
if not, return the smalleest one found


NOTE: it does go dowqn the line, if the first recur call
does not work out
NOTE: whats different is this return structure


Top-down INTUTION:
- current start == end, call [start+1][end-1], if that returns True, then True
- current start != end, call [start][end-1] and [start+1][end]
                        record the max of these

Bottom-up INTUITION:
- only switching to Trues
- only check [start+1][end-1] (should be filled)

Counting, instead of longest:
- everytime True, increment count

Minimum deletions:
- the longest is minimum deletion
- len(st) - longest


"""

def lps(st):
    return recur(st, 0, len(st)-1)

def recur(st, start, end):
    if start > end:
        return 0
    
    if start == end:
        return 1
    
    if st[start] == st[end]:
        remain = end - start -1

        if remain == recur(st, start+1, end-1):
            return remain+2
    
    c1 = recur(st, start+1, end)
    c2 = recur(st, start, end-1)

    return max(c1, c2)


"""
Top-Down"""


def lps2(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return recur(dp, st, 0, n-1)

def recur(dp, st, start, end):
    if start > end:
        return 0
    
    if start == end:
        return 1
    
    if dp[start][end] == -1:
        if st[start] == st[end]:
            remain = end - start -1

            if remain == recur(dp, st, start+1, end-1):
                dp[start][end] = remain +2
                return dp[start][end]
        
        c1 = recur(st, start+1, end)
        c2 = recur(st, start, end-1)

        dp[start][end] =  max(c1, c2)

    return dp[start][end]


"""Bottom-up
- similar logic to palindrom subseq
- instead use T or F
- and if match, then check if diagonal down is also True
- if not  = False
- if not match, then move on

"""

def lps3(st):
    n = len(st)

    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
    
    maxed = 1

    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                #two char string
                #smaller version also palindrome
                if end-start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    maxed = max(maxed, end-start+1)

    return maxed