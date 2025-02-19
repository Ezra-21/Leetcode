class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        target = nums[len(nums)//2]
        ans = 0
        for val in nums:
            ans+=(abs(val-target))

        return ans