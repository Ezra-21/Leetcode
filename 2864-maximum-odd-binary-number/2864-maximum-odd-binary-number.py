class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = s.count('1')
        count_0 = len(s)-count_1 

        ans = []
        for i in range(count_1-1):
            ans.append('1')

        for i in range(count_0):
            ans.append('0')

        ans.append('1')

        return ''.join(ans)


        