"""
Given: set of positive number
Want: total number of subsets, with target sum

Idea:
similar to the sum
fill out the table
go up the column, for each True, backtrack

Approach:
- instead of keeping True or False
- now keep the number of subsets possible
- at each cell, add up the sum of subsets from the two locations
"""