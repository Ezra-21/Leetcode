class Solution:
    
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans,check,j = 0,0,0

        for i,num in enumerate(nums):
            while check&num:
                check^=nums[j]
                j+=1
            check|=num
            ans = max(ans,i-j+1)

        return ans
            
