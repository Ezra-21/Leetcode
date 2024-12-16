class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        valid_subarray = 0
        start,end = -1,-1
        for i in range(len(nums)):
            if left<=nums[i]<=right:
                end=i
            elif nums[i]>right:
                start = i
                end = i

            valid_subarray+=(end-start)

        return valid_subarray
            

        