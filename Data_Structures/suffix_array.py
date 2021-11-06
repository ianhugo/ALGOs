"""
suffix: substring
at the end of a string of characters

suffix array:
contain all lexicographically- sorted suffixes of a string
array of sorted indices (corresponding to the suffixes)
(reltead to suffix tree and trie)
------

Longest Common Prefix (LCP) array:
each index, store how many characters, two suffixes share
(this and the one before)
in terms of prefixes
so starting from the left

after sorted suffix array
at each index, the number of suffix characters share 
with the one previously

set the first index as 0 or None
-------

Finding Unique Substrings
naive: O(n^2)

number of substrings: n(n+1)/2
but there could be duplicate ones

unique = (number of substrings) - sum(LCP[i])

--------
USES:
as the suffix array is sorted
can use binary search to find a particular suffix

---------
Construction efficient O (n lg n)

1: sort lexicographically
- create a trie
- do DFS on trie, add each to list when reach terminal
(https://stackoverflow.com/questions/10057537/lexicographical-sorting-of-word-list)


or 
sorted(s, key=str.lower)
sorted(s, key=str.upper)
sorted(sorted(s), key=str.upper)

or
-----------
CONSTRUCTING SUFFIX ARRAY
(https://www.youtube.com/watch?v=_TUeAdu-U_k)
1: represent each character as a number (based on alphabet)
2: now can compare the first letter of each suffix
(note suffixes are a increasingly small window of words)
sort these and get ordering 1
3: now consider first two characters as tuples
sort these and get ordering 2
4: now extending this, if we want to compare 4 chars
for first suffix, we can take ordering2[0] and ordering2[2]
CUZ: ordering2 represents the ordering of 2 char positions
together they represent first 4 characters (wow)
(NOTE: important bit is constructing these tuples)
5: and we sort again
and we keep extending
6: we can terminate if at any point the numbers in the
new ordering array is unique
7: now we can construct the suffix array
by taking the values in our latest ordering arr
which is indexed as per the original position of input arr
we use the values, to put the original indexes
in a new order
in a suffix arr !!

if use merge sort O(n lg^2 n)
we can use radix sort to get O(n)


RUNTIME ANALYSIS:
ordering among first order
then ordering of first two
then ordering of first four
pattern: factors of 2
total iterations until guarantee = O(lg n)

"""

class Suffix_Array:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.suffix_arr = None
        self.lcp_arr = None
        self.constructed_SA = None
        self.constructed_LCP = None
    
    def build_SA(self):
        if self.constructed_SA:
            return
        self.consturct()
        self.constructed_SA = True
    
    def build_LCP(self):
        if self.constructed_LCP:
            return
        self.build_SA()
        self.kasai()
        self.constructed_LCP = True
    
    def deconstruct(self, string):
        if string == None:
            return None
        
        t = []
        for i in range(len(string)):
            t[i] = string[i]
        
        return t
    
    def construct(self):
        pass
    
    #Kasai algo to build LCP

    """
    Kasai algo to build LCP
    
    https://www.coursera.org/lecture/algorithms-on-strings/computing-the-lcp-array-HyUlH
    start by comparing suffix_array[0] and suffix_array[1]
    get their LCP
    now move suffix_array[0] right one on the original array (unsorted but with decreasing suffixes)
    and compare it to its right neighbor in the suffix array
    (it is a strange but good order)
    (can avoid some comparisons)
    repeat until LCP full
    each iteration, length of LCP decrease by at most 1
    (as we only cut away one)

    this is done in O(n)
    why? because of bounds on length of prefix and 
    """

    def kasai(self):
        lcp_arr = [None]*self.n
        inv = [None]*self.n

        for i in range(self.n):
            inv[self.suffix_arr[i]] = i
        lent = 0
        for i in range(self.n):
            if inv[i] > 0:  #first lcp = 0 always
                k = self.suffix_arr[inv[i]-1] #previoius suffix
                #not out of bounds
                # not out of bounds
                #values match
                while (i + lent < self.n) and (k + lent < self.n) and (self.arr[i+lent] == self.arr[k+lent]):
                    lent += 1   #match thus increment
                self.lcp_arr[inv[i]] = lent
                if lent >0: #when move to next 
                    lent -= 1
