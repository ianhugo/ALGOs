"""
GIVEN: array with two numbers not repeated twice
WANT: those two numbers

(https://www.youtube.com/watch?v=L-EaPf5tD5A)

APPROACH
- go through once XOR, result is a XOR b

result = if has 1, x and y have different bits
result = if has 0, x and y have same bits

a XOR a = 0
means: two same bits cancel each other
means: set bits in XOR, occur odd number of times in array

so: select any set bit of XOR
so: choose lowest set bit

SHORTCUT:
lowest set bit = result & (-result)
then add 1 to it

SLOW:
compare one with each bit in mask
if no match, left shift
if match, stop

have bit at which x and y differ

so: iterate through again, to get the first element
if number & low-bit mask == 0
= separate numbers into two parts
= with the two numbers in different groups
(note that other numbers appear twice, thus will cancel out)
= keep XOR-ing into two containers = get two numbers

WHY: only need one position

"""

def solve(nums):
    xy = 0

    for num in nums:
        xy ^= num   #result in x^y
    
    xy &= -xy       #bitmask at first position x y differ

    result = [0, 0]

    for num in nums:
        if xy & num:
            result[0] ^= num
        else:
            result[1] ^= num

            #or result[0]^xy = result[1]

#getting last set bit
# xy1 =  xy & (xy-1)
#xy1 ^= xy