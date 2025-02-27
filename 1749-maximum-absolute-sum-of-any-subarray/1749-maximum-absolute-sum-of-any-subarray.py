class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)