class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        prev1,prev2 = 0,1
        
        for i in range(2,n+1):
            temp = prev1+prev2
            prev1 = prev2
            prev2 = temp
        return prev2

        