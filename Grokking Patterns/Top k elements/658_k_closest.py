"""
Given: sorted array, int k, int x
WANT: k closest ints to x in the array
ascecnding order

a is closer to x if

|a - x| < |b - x|
|a - x| == | b - x|, and a < b

IDEA:
define function that compares this

as iterate, push the closer number to max heap
store the difference
compare new to the top of max

APPROACH:
- instead of iterate through
- use binary search
- find closest to x = y (adj to x)
- take K on both sides
- iterate into min heap
- pop as needed

"""