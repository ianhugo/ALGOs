"""
Given: number
Want: complement

0 ^ x = x
1 ^ x - 1-x (flips the bit)

<< = add 0 to right, push left
>> = add 0 to left, push right
"""

#Flip bit by bit

def complement(num):
    todo, bit = num, 1

    while todo:

        #flip current bit
        num = num ^ bit

        #move to next bit
        bit = bit << 1

        #iterate counter
        #want this to become 0 = False
        #when have processed all bits
        todo = todo >> 1
    
    return num

#compute bitmask
import math
from math import log2, floor
def complement2(num):
    #get length
    n = floor(log2(num)) + 1

    #construct bitmask
    bitmask = (1 << n) - 1 #-1 to get all 1-es

    #flip all bits
    return bitmask ^ num