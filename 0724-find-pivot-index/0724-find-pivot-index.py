class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum,right_sum = 0,sum(nums)
        for i in range(len(nums)):
            if i != 0:
                left_sum+=nums[i-1]
            right_sum-=nums[i]
            if left_sum == right_sum:
                return i

        return -1
            
        