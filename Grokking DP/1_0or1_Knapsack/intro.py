"""
Given:
- array of things
- want some combination to fulfill some constraint
- choose or not choose

DP Table
- the basic form is True or False
- but can store more information also
    - for example: if True, then store a value, if not then -1
- rows = candidates to include
- columns = the attribute being constrained
- columns L to R = building towards the target constraint
- use:  for this candidate i (row i)
        should it be included in an optimal sol
        if constrained at attribute1 value j (column j)
        if yes, put True (or the "result" of such includion)
        if no, put False
        to find the next included item
        go to column (constraint_v - j) 
- implement:    consider one item for all possible constraint values
                move to next row
                (each new row is adding new items to the candidate "subset")
                at each cell, check for 
                exclude: dp[i-1][s]
                include: self + dp[i-1][s-val[i]]  subtract value of i
- note: have to pad values for logic to start off

- note: for each cell refer to two previous values
- thus can do space compression
- use (i-1)%2 = previous
- use (i)%2 = current
- why? dynamically know which is curr/prev
- don't need to copy and paste stuff around
- absolute: use one row only, go from row[][-1] to row[][0]
- works as: always refer to two previous values


Top-DOwn:
- include, exclude recursive calls
- take max on callback

Backtracking:
- if same as above, then excluded, took value from above

Time Complexity = fill out dp table 
O(n x c)
c = "capacities"

-----------------------
Pattern 1
- one attribute
- include or not include to get to a target
- booleans

-----------------------
Pattern 2
- two attributes
- constraint on attribute 1
- optimized at each cell of attribute 2 (max/min/sth else)

-----------------------
Pattern 3
- count all possible
- store the number of possible subsets
- at each, sum up from both locations

-----------------------
Pattern 4
- math things out to map to pattern

Observation:
- divide up responsibilities between minions
- don't pass around res array
- can be implicit in the dp table 

"""