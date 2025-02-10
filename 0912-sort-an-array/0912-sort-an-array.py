class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        min_val, max_val = min(nums), max(nums)
        count = [0] * (max_val - min_val + 1)
        
        for num in nums:
            count[num - min_val] += 1
        
        index = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[index] = i + min_val
                index += 1
                count[i] -= 1
        
        return nums