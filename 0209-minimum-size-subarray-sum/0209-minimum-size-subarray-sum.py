class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans,summ,j = sum(nums),0,0
        if ans < target: return 0
        if ans == target: return len(nums)
        for i in range(len(nums)):
            summ += nums[i]
            while summ >= target:
                ans = min(ans,i-j+1)
                summ -= nums[j]
                j += 1
        return ans
            