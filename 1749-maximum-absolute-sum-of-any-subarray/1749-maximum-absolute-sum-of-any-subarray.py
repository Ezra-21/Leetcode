class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_min,prefix_max = 0,0
        summ = 0
        for num in nums:
            summ+=num
            prefix_min = min(prefix_min,summ)
            prefix_max = max(prefix_max,summ)
            
        return prefix_max-prefix_min