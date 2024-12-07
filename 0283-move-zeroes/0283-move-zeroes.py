class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                left = i
                break
        if left == -1:
            return nums
        right = left+1
        while right<len(nums):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
            right+=1
        return nums
        