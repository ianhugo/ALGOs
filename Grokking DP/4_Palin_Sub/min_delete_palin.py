"""
Given: string
Want: minimum deletion to make palin subseq

IDEA:
use original LPS strategy (516), find that
longest palindromic subsequence
would mean, the least number of deletions
include the most of original characters

so do length(st) - LPS length
"""