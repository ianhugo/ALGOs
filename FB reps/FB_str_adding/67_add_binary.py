"""
GIVEN: 2 binary strings
WANT: sum as binary string


Basic:
- position by position
- note the carry
- add last bit of carry
"""

"""
#loop through each unit
#first iteration: 
- get ans without carry
- get the carry

now, need to put the carry in
- so keep going, same process
"""


def add(a, b):
    x, y = int(a, 2), int(b, 2)

    #x = ans
    #y = carry

    while y:    #while non-zero carry
        ans = x^y #curr ans without carry
        carry= (x&y) << 1 #current carry

        x,y = ans, carry
    
    return bin(x)[2:]