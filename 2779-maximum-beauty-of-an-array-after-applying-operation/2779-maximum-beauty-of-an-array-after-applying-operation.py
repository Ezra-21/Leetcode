class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        j = 0
        for i in range(1,len(nums)):
            while nums[i] - nums[j] > 2*k:
                j+=1

            ans = max(ans,i-j+1)
            
        return ans


        

        


        