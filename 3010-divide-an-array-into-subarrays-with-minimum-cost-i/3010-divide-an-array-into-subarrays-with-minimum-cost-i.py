class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        rest = nums[1:]
        
        rest.sort()
        
        return first + rest[0] + rest[1]

        