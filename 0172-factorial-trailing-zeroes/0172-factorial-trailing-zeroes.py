class Solution:
    def fac(self,n):
        if n<=1:
            return 1
        return n*self.fac(n-1)

    def trailingZeroes(self, n: int) -> int:
        result = self.fac(n)
        count_0 = 0
        while result:
            last = result%10
            if last == 0:
                count_0+=1
            else:
                break
            result //= 10

        return count_0
