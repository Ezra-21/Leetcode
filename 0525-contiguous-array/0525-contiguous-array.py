class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashh = {0:-1}
        nums = nums
        max_len = 0
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i] = -1
            if i>0:
                nums[i]+=nums[i-1]
          
            if nums[i] not in hashh:
                hashh[nums[i]] = i
            else:
                max_len = max(max_len,i-hashh[nums[i]])

        return max_len

        