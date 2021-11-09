"""
find longest common substring between k of n strings

n > k >= 2

n1 = length of string 1
DP: O(n1 * n2 . . .)
suffix = O(n1 + n2 . . .)

1: concatenate, separated by unique sentinels
2: construct suffix array
3: construct lcp array
"""