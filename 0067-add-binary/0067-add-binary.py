class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a,b = a[::-1],b[::-1]
        res = ''
        for i in range(max(len(a),len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry

            summ = total & 1 # same as summ = total % 2

            res = str(summ)+res

            carry = total >> 1 # same as summ = total // 2
            
        if carry == 1:
            res = '1'+res

        return res
