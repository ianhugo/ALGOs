"""
Motivation:
given array of integers
query sum of range
?compute prefix sums = O(1)
?what if update tho, prefix sums have to recompute :(

support range queries
and point updates

Construction: O(n)
Point update, range sum, range update: O(lg n)

but cannot ADD or REMOVE

FENWICK TREE
each cell: responsible for range of other cells
cell responsibility: depending on binary rep
least significant bit

EXAMPLE:
index 12 = binary 1100
LSB = position 3
(LSB = bit position giving units value
determining even or odd)
(first digit that is not a 0)
Index 12 is responsible for
2^(3-1) = 4 
4 cells below itself

NOTE: all odd numbers have LSB in position 1
only responsible for themselves

NOTE: range of responsibilites in powers of 2
------------------
RANGE QUERIES:
compute prefix sum, up to certain index

EXAMPLE:
find prefix sumn up to index 7, inclusive
add it
cascade downwards, then hop

Interval:
calculate two prefix sums
but exclusive with one of them

Worst Case: 
query indexes with binary rep = all 1-es
(numbers of form 2^n -1)
(or ones with a lot of 1-es)
might have to do two queries costing log(n) operations
(hitting a lot of these bad indexes)

-----------------
POINT UPDATES:
adding values in

need to propagate value up, 
to cells responsible for updated cells
skipping up at powers of 2

------------------
CONSTRUCTION:
naive: O(n lg n)
better: O(n)

IDEA:
propagate values upwards
point updates, one at a time

EXAMPLE:
if currently at i
immediate next cell to update
j = i + LSB(i)
(just update the parent, immediate cell above)
(watch out for boundaries)

"""
def ffs(x):
    """Returns the index, counting from 0, of the
    least significant set bit in `x`.
    """
    return (x&-x).bit_length()-1

def lsb(i)
class Fenwick_Tree():
    def __init__(self):
        self.size = None
        self.arr = None
        self.lent = None
        self.tree = None
    
    def build(self):
        self.lent = len(self.arr)
        self.tree = self.arr.copy()
        for i in range(self.lent):
            j = i + ffs(i)
            if j < self.lent:
                self.tree[j] += self.tree[i]

    def prefix_sum(self, i):
        sum = 0
        while i != 0:   #add as cascade down
            sum += self.tree[i]
            i -= ffs(i)

        return sum

    def interval_sum(self, i, j):
        if j < i:
            print("must be valid range")

            return self.prefix_sum(j) - self.prefix_sum(i)
    
    #add to it
    def add(self, i, k):
        while i< self.lent:
            self.tree[i] += k
            i += self.ffs(i)
    
    #set it to new
    def set(self, i, k):
        value = self.sum(i, i)
        self.add(i, k-value)
