class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        summ = 0
        for i in range(len(nums)):
            if i >= k and nums[i] <= nums[i-k]:
                continue
            if i+k<len(nums) and nums[i]<= nums[i+k]:
                continue
            summ += nums[i]
        return summ