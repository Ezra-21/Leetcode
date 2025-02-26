class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        ans = float('-inf')
        for i in range(len(nums)):
            summ+=nums[i]
            ans = max(ans,summ)
            if summ<0:
                summ = 0

        return ans