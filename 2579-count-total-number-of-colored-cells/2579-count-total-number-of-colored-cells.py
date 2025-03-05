class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        for i in range(1,n):
            ans += (i*4)

        return ans