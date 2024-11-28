class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Modify nums in-place to follow the wiggle sort pattern.
        """
        nums.sort()
        mid = (len(nums)+1)//2

        first_smaller = nums[:mid][::-1]
        last_largest = nums[mid:][::-1]

        nums[::2] = first_smaller
        nums[1::2] = last_largest



        
