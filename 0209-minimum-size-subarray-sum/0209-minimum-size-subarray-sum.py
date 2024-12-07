class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        summ = 0
        j = 0
        for i in range(len(nums)):
            summ+=nums[i]
            
            while summ>=target:
                ans = min(ans,(i-j+1))
                summ -= nums[j]
                j+=1
        
        return 0 if ans == float('inf') else ans
