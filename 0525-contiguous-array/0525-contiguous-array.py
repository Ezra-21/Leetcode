class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i] = -1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        nums = [0]+nums

        hashh = {}
        for i,val in enumerate(nums):
            hashh[val] = i

        max_len = 0
        for i,val in enumerate(nums):
            max_len = max(max_len,(hashh[val]-i))

        return max_len