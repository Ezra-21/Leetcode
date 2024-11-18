class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        maxlen = sum(nums)
        count = sum(nums[:maxlen])
        maxone = count
        left,right = 0,maxlen
        while right < 2* len(nums):
            count += nums[right%len(nums)]
            count -= nums[left%len(nums)]
            maxone = max(maxone,count)
            right += 1
            left += 1

        return maxlen - maxone
        
            