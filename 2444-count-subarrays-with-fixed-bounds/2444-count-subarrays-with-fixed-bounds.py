class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_pos = max_pos = invalid_pos = -1
        ans = 0
        
        for i, val in enumerate(nums):
            if val < minK or val > maxK:
                invalid_pos = i  
                
            if val == minK:
                min_pos = i  
            if val == maxK:
                max_pos = i  

            ans += max(0, min(min_pos, max_pos) - invalid_pos)
        
        return ans
