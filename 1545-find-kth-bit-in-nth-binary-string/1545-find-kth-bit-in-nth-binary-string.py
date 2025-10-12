class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return '0'

            res = helper(n-1)
            temp = ''
            for ch in res:
                if ch == '0':
                    temp+='1'
                else:
                    temp+='0'
                
            res = res+'1'+temp[::-1]
            return res
        
        return helper(n)[k-1]
        