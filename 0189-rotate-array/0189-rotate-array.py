class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        num = nums[-k:]+nums[:-k]
        for i in range(len(nums)):
            nums[i] = num[i]
        