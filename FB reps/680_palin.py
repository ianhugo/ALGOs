"""
Given: str
Want: bool, if delete at most one char

Idea:
two pointers
if matched continue
if unmatched, decrement allowance
(which one is the right one?)
(need to try both)
if unmatched again, break
if finish, return True
"""