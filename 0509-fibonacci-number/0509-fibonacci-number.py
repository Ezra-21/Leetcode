class Solution:
    def fib(self, n: int) -> int:
        f = [0,1]
        for i in range(2,n+1):
            f[i] = self.fib(n-1)+self.fib(n-2)
        
        return f[n]

        