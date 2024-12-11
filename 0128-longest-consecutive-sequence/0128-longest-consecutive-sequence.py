class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        nums = list(set(nums))
        nums.sort()
        
        j = 0
        for i in range(1,len(nums)):
            if nums[i]!= nums[i-1]+1:
                j = i
            ans = max(ans,i-j+1)

        return ans
            
            
        