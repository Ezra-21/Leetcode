class Solution:
    def fib(self, n: int , dic={}) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n in dic:
            return dic[n]

        dic[n] = self.fib(n-1,dic)+self.fib(n-2,dic)

        return dic[n]

        