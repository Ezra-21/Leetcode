class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for j in range(len(nums)):
            if nums[j]==0:
                index = j
                break
        if index != -1:
            for i in range(index+1,len(nums)):
                if nums[i] != 0:
                    nums[i],nums[index] = nums[index],nums[i]
                    index+=1
        return nums
        