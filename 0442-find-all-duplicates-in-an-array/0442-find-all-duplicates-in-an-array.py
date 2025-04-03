class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        start = 0
        ans = []
        while start < len(nums):
            position = nums[start] - 1
            if nums[start] != nums[position]:
                nums[start], nums[position] = nums[position], nums[start]   
            else:
                start += 1
            
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(nums[i])

        return ans
        