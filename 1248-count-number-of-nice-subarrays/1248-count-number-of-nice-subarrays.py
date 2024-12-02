class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        
        count_odd =  ans = 0
        valid_subarray = 0

        j = 0
        for i in range(len(nums)):
            if nums[i] %2 ==1:
                count_odd += 1
                valid_subarray = 0
            
            while count_odd == k:
                valid_subarray += 1

                if nums[j] %2 ==1:
                    count_odd -= 1

                j+=1
                
            ans += valid_subarray

        return ans

                
