"""

BASIC:
XOR of bit and zero = bit
XOR of bit and bit = zero

IDEA: mark opposite bit positions as 1

BASIC 2:
chaining XOR
A ^ A = 0
0 ^ B = B
can find the odd one out

BASIC 3:
memory property

BASCI 4:
Associative (parentheses do not change)
Commutative (order does not matter)


-----------------------
^ operator

USES:
1. Bitmask
on -> off
off -> on

2. Cryptography
- use bitmask as a key
- done quickly
- same key used to reverse


-----------------------

APPROACHES:
1. Find non-duplciate number
- XOR into running constant
- if did not appear twice = the missing one = remaining value


-----------------------

2. Find 2 non-duplicated numbers
- XOR into running constant
- result = a^b
- diffrentiate by getting difference bitmask: result&(-result)
- when iterate through again
- do difference_bitmask & curr
- True/False = will filter out two groups
- res1 or res2 ^= curr
- each group holds the number
- alternatively: number1^difference = number2


-----------------------
3. Complements
- need bits of 1 of length n
- then can flip 

NOTE: logical bit operators, turn stuff into bits in background

"""