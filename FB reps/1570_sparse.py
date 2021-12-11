"""
Given: two sparse vectors
WANT: dot product

Sparse vector: mostly zero values
store this efficiently

Dot product:
v1[i]* v2[i] + v1[i+1]* v2[i+1]

WANT: data object class
WANT: dot product method


IDEA:
- store non-zero values, in hash

"""

#hash might take a lot of time if big sparse vector

class Sparse:
    def __init__(self, nums):
        self.store = {}
        for i,n in enumerate(nums):
            if n!= 0:
                self.store[i] = n
    
    def dot(self, vec):
        result = 0

        for i, n in self.store.items():
            if i in vec.store:
                result += n* vec.store[i]
        return result

#might be more efficietn
class Sparsey:
    def __init__(self, nums):
        self.pairs = []
        for i,v in enumerate(nums):
            if v != 0:
                self.pairs.append([i,v])
        
    def dot(self, vec):
        res = 0
        p,q = 0,0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                res += self.pairs[p][1] * self.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1
        
        return res