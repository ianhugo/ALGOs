import math

class Sparse_Table():
    def __init__(self):
        self.input_len = None
        self.power = None
        self.max_power = None
        self.log2_lookup = None
        self.sparse_t = []
        self.index_t = []
        self.operation = None

    
    def sum_t(self, a, b):
        return a + b
    
    def min_t(self, a, b):
        return min(a, b)
    
    def max_t(self, a, b):
        return max(a, b)
    
    def mult_t(self, a, b):
        return a*b

    def gcd_t(self, a, b):
        gcd = a
        while b != 0:
            gcd = b
            b = a % b
            a = gcd
        return abs(gcd)
    
    def init(self, arr):
        self.power = 2
        self.input_len = len(arr)
        self.max_power = math.log(self.input_ln)/ math.log(self.power)

        for i in range(self.input_len): #populate sparse_t and index
            self.sparse_t[0][i] = arr[i]
            self.index_t[0][i] = i
        
        self.log2 = []
        for i in range(2, self.input_len): #populate log 2 array
            self.log2[i] = self.log2[i/2]+1
        
        
        for i in range(self.max_power):
            j = 0
            while (j+(1<<i)) <= self.input_len:
                left_interval = self.sparse_t[i-1][i]
                right_interval = self.sparse_t[i-1][j+ (1<< (i-1))]
                if self.operation == "MIN":
                    self.sparse_t[i][j] = self.min_t(left_interval, right_interval)
                    if left_interval <= right_interval:
                        self.index_t[i][j] = self.index_t[i-1][j]
                    else:
                        self.index_t[i][j] = self.index_t[i-1][j+(1<< (i-1))]
                elif self.operation =="Max":
                    self.sparse_t[i][j] = self.max_t(left_interval, right_interval)
                    if left_interval <= right_interval:
                        self.index_t[i][j] = self.index_t[i-1][j]
                    else:
                        self.index_t[i][j] = self.index_t[i-1][j+(1<< (i-1))]
                elif self.operation == "SUM":
                    self.sparse_t[i][j] = self.sum_t(left_interval, right_interval)
                elif self.operation == "MULT":
                    self.sparse_t[i][j] = self.mult_t(left_interval, right_interval)
                elif self.operation == "GCD":
                    self.sparse_t[i][j] = self.gcd_t(left_interval, right_interval)
                    

                j += 1

    def query(self, l, r):
        if self.operation == "MIN":
            return self.query_priv(l, r, self.min_t)
        elif self.operation == "MAX":
            return self.query_priv(l, r, self.max_t)
        elif self.operation == "GCD":
            return self.query_priv(l, r, self.gcd_t)
        elif self.operation == "SUM":
            return self.sum_q(l, r)
        else:
            return self.mult_q(l, r)
    
    def query_index(self, l, r):
        if self.operation == "MIN":
            return self.min_q_index(l, r)
        elif self.operation == "MAX":
            return self.max_q_index(l, r)
    
    def min_q_index(self, l, r):
        lent = r - l +1
        p = self.log2[lent]
        left_interval = self.sparse_t[p][l]
        right_interval = self.sparse_t[p][r -1 ( 1<<p)+1]
        if left_interval<= right_interval:
            return self.index_t[p][l]
        else:
            return self.index_t[p][r-(1<<p)+1]
    
    def max_q_index(self, l, r):
        lent = r - l +1
        p = self.log2[lent]
        left_interval = self.sparse_t[p][l]
        right_interval = self.sparse_t[p][r -1 ( 1<<p)+1]
        if left_interval>= right_interval:
            return self.index_t[p][l]
        else:
            return self.index_t[p][r-(1<<p)+1]       
    
    def sum_q(self, l, r):
        sum = 0
        p = self.log2[r-l+1]
        while l<= r:
            sum += self.sparse_t[p][l]
            l += (1<<p)
        
        return sum
    
    def mul_q(self, l, r):
        res = 1
        p = self.log2[r-l+1]
        while l<= r:
            res += self.sparse_t[p][l]
            l += (1<<p)
        
        return res

    def query_priv(self, l, r, operation):
        lent = r - l +1
        p = self.log2[lent]
        ll = self.sparse_t[p][l]
        rr = self.sparse_t[p][r - (1<<p)+1]
        return operation(ll, rr)
    

