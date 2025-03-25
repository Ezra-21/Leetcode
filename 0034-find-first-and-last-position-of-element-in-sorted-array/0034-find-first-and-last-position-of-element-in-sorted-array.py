class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [-1,-1] if target not in nums else [bisect_left(nums,target),bisect_right(nums,target)-1]