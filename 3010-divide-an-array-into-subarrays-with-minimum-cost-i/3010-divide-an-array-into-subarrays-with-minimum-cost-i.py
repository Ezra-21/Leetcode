class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        num1 = nums[0]
        num2 = min(nums[1:])
        idx = (nums[1:].index(num2))+1
        
        if idx-1 == 0:
            num3 = min(nums[idx+1:])
        elif idx == len(nums)-1:
            num3 = min(nums[1:idx])
        else:
            num3 = min(min(nums[1:idx]),min(nums[idx+1:]))
        return num1+num2+num3