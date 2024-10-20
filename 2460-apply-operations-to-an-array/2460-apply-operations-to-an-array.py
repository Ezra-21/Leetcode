class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        left = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                left = i
                break
        if left != -1
            for right in range(left+1,len(nums)):
                if nums[right] != 0: 
                    nums[left],nums[right] = nums[right],nums[left]
                    left += 1
        
        return nums

        