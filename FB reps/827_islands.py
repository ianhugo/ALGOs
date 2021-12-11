"""
Given: nxn matrix of 0-es and 1-es
Want: largest area of 1-es

STRATEGY:
PART 1:
- find all islands
- assign number
- memoize size

PART 2:
- check each empty cell's 4 neighbors
- create set of unique islands
- evaluate sum of sizes of all neighbors
- return biggest

"""

from collections import Counter
#dict of counting

from itertools import product
#create all pairs/dot product

class Solve:
    def __init__(self):
        pass

    def larges(self, grid):
        
        self.grid = grid

        self.m, self.n = len(grid), len(grid[0])

        self.neib = [[1,0],[-1,0],[0,-1],[0,1]]

        self.islands, self.count, self.res = Counter(), 2, 0   


        for x,y in product(range(self.m), range(self.n)):
            if self.grid[x][y] ==1:
                self.dfs(self.count, x, y)
                self.count += 1
        
        #finding the biggest island
        for x,y in product(range(self.m), range(self.n)):
            if self.grid[x][y] != 0:
                continue

            self.neib2 = set()

            #explore spots around empty
            for dx, dy in self.neib:
                if (0 <= x + dx < self.m) and (0 <= y + dy< self.n) and self.grid[x+dx][y+dy] != 0:
                    self.neib2.add(grid[x+dx][y+dy])
            
            self.res = max(self.res, sum(self.islands[i] for i in self.neib2)+1)
        
        return self.res if self.res != 0 else self.m * self.n

    def dfs(self, t, i, j):
        #not out of bounds, and is a valid 
        if not (0 <= i < self.m) or not (0 <= j < self.n) or self.grid[i][j] != 1:
            return
        
        self.islands[t] += 1
        self.grid[i][j] = t

        for x, y in self.neib:  #explore surrounding
            self.dfs(t, x+i, y+j)
