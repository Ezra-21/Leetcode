class Solution:
    def solve(self,s,n):
        if n==1:
            return s
        t =  ''.join('1' if ch == '0' else '0' for ch in s)[::-1]
        s = s + '1' + t
        return self.solve(s,n-1)

    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        s = self.solve(s,n)
        print(s)

        return s[k-1]