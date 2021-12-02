
"""
Recursive INtuition:
- set min cuts to length (cut everywhere)
- iterate through to find a point to cut
    that creates palin LHS
- check if can cut here, [start][i] = palindrome?
- if so, recursively check for (start+1, end)
- base case = at 0, or is a palindrome
    return 0
- recursse back = return mincuts of this (start, end) 
- on call back, take min(running_min, 1+returned)

Top-Down Memoization:
- dp[i][j] = min cuts of piece [i:j] to palindrome
- palin[i][j] = it is palin slice
- check dp
- cache dp

Bottom-Up:
- build palin[i][j] table
    (finding subsequence)
"""
"""BRUTE"""
def cuts(st):
    return recur(st, 0, len(st)-1)

def recur(st, start, end):

    if start >= end or check(st, start, end):
        return 0
    
    #at max, cut into 1 length pieces
    mincuts = end - start

    for i in range(start, end+1):
        if check(st, start, i):
            #can cut here, as palin
            #everytime find palin, go down the line
            #see how many potential cuts afterwards
            #recurse back
            #find minimum
            mincuts = min(mincuts, 1+recur(st, i+1, end))
    
    return mincuts

def check(st, x, y):
    while(x <y):
        if st[x] != st[y]:
            return False
        
        x+= 1
        y-= 1
    
    return True




"""TOP-DOWN"""

def cuts2(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    dp_palin = [[-1 for _ in range(n)] for _ in range(n)]

    return recur2(dp, dp_palin, st, 0, n-1)

def recur2(dp, dp_palin, st, start, end):

    if start >= end or check(dp_palin, st, start, end):
        return 0
    
    if dp[start][end] == -1:

        mincuts = end - start

        for i in range(start, end+1):
            if check2(dp_palin, st, start, i):
                mincuts = min(mincuts,\
                    1+ recur2(dp, dp_palin, st, i+1, end))
        
        dp[start][end] = mincuts
    
    return dp[start][end]


#this part is bottom up?
def check2(dp_palin, st, x, y):

    if dp_palin[x][y] == -1:
        dp_palin[x][y] = 1
        i, j = x, y

        while i < j:
            if st[i] != st[j]:      #if one unmatched, immediately 0, which is faalse
                dp_palin[x][y] = 0
                break
            i += 1  #iteration things
            j -= 1

            #if matched
            #valid smaller window
            #and smaller window checked
            #if not, check on next loop
            if i<j and dp_palin[i][j] != -1:    #if it has been checked
                dp_palin[x][y] = dp_palin[i][j]
                break

            #if not checked? keep going util the end
            #if reach the end, still ok, then it is palindrom
            #question, why not store some intermediate results as well: useless as they will be one-off
            #every sub palindrome, can only belong to one larger palindrom
            #but it might still be helpful
    return True if dp_palin[x][y] ==1 else False


"""Bottom-Up

O(n^2)"""

def cuts3(st):
    n = len(st)

    is_palin = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        is_palin[i][i] = True
    
    #normal palin subseq
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                if end - start == 1 or is_palin[start+1][end-1]:
                    is_palin[start][end] = True

    cuts = [0 for _ in range(n)]
    #every index = min cuts for st[index:]
    #as going up the dp table
    #increasing towards the full string


    #iterate rows, from bottom to up
    for start in range(n-1, -1, -1):
        mincuts = n

        #each row, iterate from end to diagonal
        for end in range(n-1, start-1, -1):

            #if get a palindrome, cut string
            #min cuts = 1 + cuts for remaining
            #moving back to front

            if is_palin[start][end]: #if palindrome
                #if at this row, st[row][curr] == palin
                #then add the result from before
                #just need one cut

                #so at any point, taking the largest piece 
                #we can find on this row
                #then adding it to the previous result
                if end == n-1: #starting
                    mincuts = 0 
                else:   #cut here
                    mincuts = min(mincuts, 1 + cuts[end+1])
        
        cuts[start] = mincuts
    
    return cuts[0]
