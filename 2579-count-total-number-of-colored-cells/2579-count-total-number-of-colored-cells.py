class Solution:
    def coloredCells(self, n: int) -> int:
        temp = 0
        def solve(temp,n):
            if n==1:
                return 1+temp
            temp+=4
            n-=1
            return solve(temp,n)
        return solve(temp,n)
             
        