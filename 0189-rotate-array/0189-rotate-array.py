class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        arr = nums[-k:] + nums[:n-k]
        for  i in range(n):
            nums[i] = arr[i]