"""
GIVEN: two integers
WANT: sum

BREAK-DOWN:
- do adds
- do minuses

Adding with XOR:
- XOR = add without carry
- x & y << 1 = carry
- recursively keep doing
- while nonzero carry

Subtravting with XOR:
- XOR = subtract without borrow
- ((~x)&y) <<1 - borrow
(common set bits of y
unset bits of x)
- recursively, while nonzero borrow

O(1)
int has 32 bits
"""

def sum(a, b):

    x, y = abs(a), abs(b)

    if x< y:    #standardize
        return sum(b, a)
    
    sign = 1 if a>0 else -1

    if a * b >= 0:  #positives
        while y:
            ans = x^y
            carry = (x&y) <<1
            x, y = ans, carry
    
    else:
        while y:
            ans = x^y
            borrow =  ((~x) & y) << 1
            x, y = ans, borrow
        
    
    return x * sign

