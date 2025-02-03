class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = {}
        for i,num in enumerate(nums):
            if target - num in hashh:
                return hashh[target-num],i
            hashh[num] = i
            
        