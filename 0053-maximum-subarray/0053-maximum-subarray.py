class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        prefix = 0
        for num in nums:
            prefix += num
            max_sum = max(max_sum,prefix)
            prefix = max(prefix,0)

        return max_sum