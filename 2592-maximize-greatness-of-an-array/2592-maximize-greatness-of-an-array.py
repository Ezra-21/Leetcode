class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        j = 0
        for i in range(1,len(nums)):
            if nums[j] < nums[i]:
                ans+=1
                j+=1
        return ans

        
        