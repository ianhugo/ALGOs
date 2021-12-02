"""
Given: stream
Want: data sdtructure frequency stack

IDEA:
keep hash map of frequencies
keep sequence number
define comparator that first does frequency, then does sequence number

if new element, push as new object, still max heap tho
so it will come out on top
O(n) space

alternate: 
"""