class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                right = i
                break
        if right != -1:
            for left in range(right+1,len(nums)):
                if nums[left] != 0:
                    nums[left],nums[right] = nums[right],nums[left]
                    right+=1

