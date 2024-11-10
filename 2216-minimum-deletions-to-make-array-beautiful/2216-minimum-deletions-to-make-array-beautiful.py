class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans,n = 0,len(nums)
        i = 0

        while i<n-1:
            if i%2 == 0 and nums[i] == nums[i+1]:
                nums.pop(i)
                ans += 1
                n -= 1
            else:
                i+=1
        
        return ans if n%2==0 else ans+1



        
        