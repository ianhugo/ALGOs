"""
Given: unsorted array, n numbers from range
Want: duplicated and missing number

Strategy:
- cyclic sort
- while loop
- check if match, if unmatched = the missing
- locate duplicate
- if located duplicate, but no missing yet, then increment i

O(n) time
O(1) space
"""