class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx-1]<0:
                return abs(nums[i])
            nums[idx-1]*=-1


        