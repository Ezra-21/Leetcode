class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = 0
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            target = nums[i+1]+nums[i+2]
            if target>nums[i]:
                ans = max(ans,target+nums[i])
        
        return ans
