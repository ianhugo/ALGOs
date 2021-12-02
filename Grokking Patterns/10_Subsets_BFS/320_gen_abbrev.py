"""
Given: word
Want: unique generalized abbreviations

generalized abbrev:
- take substrings everywhere
- for each substring, change to number of chars in substr
- replace substr
- no contiguous ones tho

Strategy:
- start with original

What branches are there?
- number of substrings
- each level = substring size
- make sure not next to each other

IDEA:
- each step: abbreviate, or skip (add new, materialize abrv)
- abbreviate = add "_" (or increment abrev count)
- stop when hit target length
- last step, everyone skips

handle contiguous:
- after skipping, cannot abbreviate again

"""

"""
O(n* 2^n) for both
"""

from collections import deque
class Abbrev:

  def __init__(self, str, start,  count):
    self.str = str  #what it looks like now
    self.start = start #where to start
                        #also when to end
    self.count = count #abbrev counts

def abbrevs(word):
    lent = len(word)
    res = []
    queue = deque()
    queue.append(Abbrev(list(), 0, 0))
    #everything is a list until the end

    while queue:
        abword = queue.popleft()
        if abword.start == lent: #just skip
            if abword.count != 0: #if still abbrevs left
                abword.str.append(str(abword.count))
            res.append("".join(abword.str))
        else: #keep appending
            
            #keep adding abrevs
            queue.append(Abbrev(list(abword.str), \
                abword.start +1, abword.count+1))
            
            #keep skiping
            if abword.count != 0: #materialize
                abword.str.append(str(abword.count))
            newword = list(abword.str)
            newword.append(word[abword.start]) #which character skipped to
            queue.append(Abbrev(newword, abword.start+1, 0)) #reset abrevs
    
    return res