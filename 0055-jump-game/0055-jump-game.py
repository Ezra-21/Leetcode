class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = 0
        while j<len(nums):
            if i<0:
                return False
            if i<nums[j]:
                i = nums[j]
            i-=1        
            j+=1

        return True