class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        j = 0
        Min = nums[j]
        for i in range(1,len(nums)):
            Max = nums[i]

            if Max-Min <= 2*k:
                ans = max(ans,i-j)
            else:
                j+=1
                Min = nums[j]
        return ans+1


        

        


        