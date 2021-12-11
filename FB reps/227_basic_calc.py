
"""
ord("65") = returns ASCII
chr() = reverses it

INTUITION:
- use stack
- use recursion

- put first element in stack
- encounter sign
- pop stack, compute when it is multiply/division
- keep appending to stack if +/-

"""
class Solve:
    def __init__(self, st):
        self.st = st
        self.n = len(st)
        self.num = 0
        self.stack = []
        self.sign = "+"
    
    #start with calc(0)
    def calc(self, idx):
        while idx < self.n:
            if self.st[idx].isdigit():  #build number
                self.num = self.num*10 + int(self.st[idx])
            elif self.st[idx] in "+-*/":
                self.comp(self.sign, self.num)
                self.num, self.sign = 0, self.st[idx]   #switchy
            elif self.st[idx] =="(":
                self.num, self.j = self.calc(idx+1)
                idx = self.j-1
            elif self.st[idx] == ")":
                self.comp(self.sign, self.num)
                return sum(self.stack), idx +1
            idx += 1
        
        self.comp(self.sign, self.num)
        
        return sum(self.stack)

    def comp(self, op, val):        #grouping multiply, division
        if op == "+": self.stack.append(val)
        if op == "-": self.stack.append(-val)
        if op == "*": self.stack.append(self.stack.pop() * val)
        if op == "/": self.stack.append(int(self.stack.pop() / val))

#https://leetcode.com/problems/basic-calculator-ii/discuss/658480/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation

