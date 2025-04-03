class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxi, diff, res = nums[0], 0, 0
        
        for val in nums[1:]:
            res = max(res, diff * val)  
            maxi = max(maxi, val)  
            diff = max(diff, maxi - val)  
            
        
        return res