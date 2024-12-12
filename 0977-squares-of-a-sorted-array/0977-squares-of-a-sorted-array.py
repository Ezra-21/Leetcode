class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for val in nums:
            ans.append(val*val)
        ans.sort()
        return ans
        