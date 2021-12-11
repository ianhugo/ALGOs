"""
Given: two string
WANT: computed, no built-in function"""


def add(num1, num2):
    
    res = []

    carry = 0
    p1 = len(num1)-1
    p2 = len(num2)-1

    #iterating backwards
    while p1 >= 0 or p2 >= 0:
        if p1 >= 0:
            x1 = ord(num1[p1]) - ord("0")
        else:
            x1 = 0
        
        if p2 >= 0:
            x2 = ord(num2[p2]) - ord("0")
        else:
            x2 = 0
        
        val = (x1 +x2 + carry) %10

        carry = (x1 +x2 +carry) //10

        res.append(val)

        p1 -= 1
        p2 -= 1

        if carry:
            res.append(carry)
        
        return "".join(str(x) for x in res[::-1])
        