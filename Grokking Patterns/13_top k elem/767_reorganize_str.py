"""
Given: string
Want: rearrange characters
no adj characters the same

IDEA:
- build max heap with most frequent
- decrement, keep for now
- pop next, decrement
- put smaller back in

EXAMPLE:
(a, 4)
(b, 2)
(c, 1)
(d, 1)

a, b, a, b, c, a, d
"""