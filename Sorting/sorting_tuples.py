


def getkey0(item):
    return item[0]

def getkey1(item):
    return item[1]

l = [(1, 1), (1, 3), (0, 4), (6, 8)]
a = sorted(l, key = getkey0)
b = sorted(a, key = getkey1)

#custom objects

class ITEM:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
    
    def __cmp__(self, other):
        if hasattr(other, "getkey"):
            return self.getkey().__cmp__(other.getkey())

    def __lt__(self, other):
        #is self less than other?
        if hasattr(other, "getkey"):
            return self.getkey() < other.getkey()
        

    def getkey(self):
        return self.char1


"""
sort by one cahracteristic first
after that, need resorting only if
position is different AND
value is different
O(n lg n) to do one pass
then O(n) to do comparisons


n = len(members)
aa = sorted(member, key = getkey0)
max = members[n].char2
members[n].good = True

for i in range(n-1, 1, -1):
    if members[i].b >= max:
"""
