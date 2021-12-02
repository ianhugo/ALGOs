"""
Given: string/sequence
Want: Palindromic substring/subsequence

Subsequence: 
- can delete things to make palindrome

Substring:
- cannot delete things


DP TABLE
- rows = start index
- columns = end index

----------------------------------------------

Pattern 1: Longest Palin Subsequence
TOP-DOWN:
- make calls on each start, end pair
- base case = invalid = 0
- base case = length1 = 1

each pair 
1: matches -> shrink on both sides recur, 2 + returned
2: non match -> recur call  = shrink from start
                            = shrink from end
                            on return, take the max

BOTTOM-UP:
- dp[i][i] = 1 length palins
- bottom to top, each row diagonal point to end
- at each point, 
- if unmatched, take the max of Left and Down
    down: dp[start+1][end] 
    left: dp[start][end-1]
- if matched, take diagonal left down
    diagonal left down: dp[start-1][end-1]

WHY only above diagonal filled:
start index must be same, or smaller than end

TIME COMPLEXITY: O(n^2) = fill table


-----------------------

Pattern 2: Longest Palin Substring
- difference, if smaller ones not exact palins = not a palin
- even if matched here, must fulfill condition
    remaining length == palindrome length in remaining

TOP-DOWN:
- make calls on each start, end pair
- base case = invalid = 0
- base case = length1 = 1

each pair:
1: matches  -> shrink on both sides
            -> remaining length = end - start -1
            -> if returned length == remaining length
            -> return 2 + remaining length
2: no match, or failed above
            -> shrink from start, recur
            -> shrink from end, recur
            -> return max

BOTTOM-UP:
- similar logic to palindrom subseq
- instead use T or F
- and if match, then check if diagonal down is also True
- update running max
- if not  = False
- if not match, then move on
- keep running max


-----------------------

Pattern 3: Count Substrings
- keep running count

-----------------------

Pattern 4: Min Deletions to Palin
- find longest palin subseq, that is the best case
- len(n) - len(longest palin)


-----------------------
Pattern 5: Palin Partitioning
- define palin checking function

BRUTE:
- base case: invalid or st[start:end] == palin
    return 0
- set running_min cuts to (end - start)
- iterate (start to end)
- check if can cut here / st[start:i] == palin?
- if True:  recursively check st[i:]
            call-back: min(running_min, 1+ returned)
- return running_min


(intuition: 
- the base case is cut everywhere (true for any level)
- anchor at start
- iterate through index, until find a place to make palin
- when do so, recurse down 
- find the min cuts for the remaining
- have a running min of cuts

intuition bottom-up
- start from the back
- find the min cuts for this smaller slice
- with larger now, check if can make a larger slice at this level
- take running min)

TOP-DOWN:
- dp[i][j] = min cuts of piece [i:j] to palindrome
- palin[i][j] = it is palin slice

checking palin memoize logic:
- palin_dp, initialized to -1
- check st[x:y]
- set prematurely palin[x][y] = 1
- keep going smaller
- if not the same, then break, mark as invalid = 0
- if already checked, non -1, take that value
- at end, if palin[x][y] == 1, return True

NOTE: why not store more results in palin_dp

BOTTOM-UP:
- use normal palin subseq logic
- fill out palin subseq dp table

- create cuts [0] * n
- represents the min number of cuts to create palins
- represents the piece of palin that can be cut, 
    paired with the min cuts of what's left (if cut the palin here)
- but take the min of each possible occurence of this (each "pairing")

(everytime find palin, see if cutting this palin here 
will lead to least number of cuts overall)

- iterate through the table above
- go from bottom to up
- anchored at that level's start (row index)(diagonal index)
- having running_min = n
- iterate from back to front, i
- once find palin[row][i] = can cut here
- consider 1+ cuts[i+1]
- take min with running_min
- at the end save cuts[row] = running_min

NOTE: is TOP-DOWN, BOTTOM-UP just inverses of each other

"""