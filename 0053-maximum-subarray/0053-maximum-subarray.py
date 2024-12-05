class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            max_sum = max(max_sum,current_sum)

            if current_sum < 0:# no need to carry -ve number
                current_sum = 0

        return max_sum

        
        