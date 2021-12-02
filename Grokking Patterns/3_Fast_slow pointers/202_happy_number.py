"""
Given: number
Want: determine if it is happy
Happy: 
1. take digits
2. square digits
3. sum squared digits
4. becomes number
5. repeat
6. if becomes 1 at any point = happy

Brute 1:
keep doing this process
see if reach 1, return
Problem: can be stuck in cycle
Question: how to detect a cycle?
- fast and slow pointers?

Thought: 
how to use fast and slow pointers to detect a cycle here
Observation: at some point, will hit number that has come before

Brute 2:
keep hash of numbers that we have seen
if newest in hash = break
Problem: how long will this take
Problem: how much space will this take

Thought:
mathematical pattern?

Observation: to be happy
need to be able to add up to 10, 100, 1000 and so on . .
what does this imply for the number that came before
it has to be x^2 + y^2 = GROUP

Can't thinkg of one

RECALIBRATE
Thought:
finding cycle, with fast and slow pointers

Thought:
it is sort of like a tree
start with root number
break down by digit
square each
then add together

Thought:
both do the operation
one does the operation twice each time
see if catch up
see if gets to 1

"""


"""
Timne Complexity: O(lg n)

use sequence behavior

"""
def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow)  # move one step
    fast = find_square_sum(find_square_sum(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
  _sum = 0
  while (num > 0):
    digit = num % 10
    _sum += digit * digit
    num //= 10
  return _sum