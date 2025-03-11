class Solution:
    def solve(self,s,n):
        if n==1:
            return s
        t = list(s)
        for i in range(len(t)):
            if t[i] == '0':
                t[i] = '1'
            else:
                t[i] = '0'
        t = ''.join(t[::-1])
        s = s + '1' + t
        return self.solve(s,n-1)

    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        s = self.solve(s,n)
        print(s)

        return s[k-1]