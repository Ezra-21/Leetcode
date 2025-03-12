class Solution:
    def maximumCount(self, nums):
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        positive_count = n - left

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1  
            else:
                right = mid - 1  
        negative_count = right + 1

        return max(positive_count, negative_count)