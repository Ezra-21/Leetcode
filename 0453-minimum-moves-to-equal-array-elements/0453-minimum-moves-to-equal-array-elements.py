class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = min(nums)
        ans = 0
        for val in nums:
            ans+=(abs(val-target))
        return ans
        