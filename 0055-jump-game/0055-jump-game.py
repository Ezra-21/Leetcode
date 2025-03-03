class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        i = 0
        while i<len(nums):
            if i>m:
                return False
            m = max(m,i+nums[i])
            if m>=len(nums):
                return True

            i+=1
        return True