"""
Given: array of ints
WANT: add 1

no addition operators and such

IDEA:
- identify right most non-9 digit
- increment 1
- change subsequent 9-es to 0
"""


def plus(digits):
    n = len(digits)

    for i in range(n):
        idx = n-1-i #iterate backwards

        if digits[idx] ==9:
            digits[idx] = 0
        else:

            digits[idx] += 1

            return digits
    
    #all digits are 9
    return [1] + digits