class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_min,curr_max = 0,0
        Max,Min = 0,0
        l = 0
        for num in nums:
            curr_max = max(curr_max+num,num)
            Max = max(Max,curr_max)

            curr_min = min(curr_min+num,num)
            Min = min(curr_min,Min)

        return max(abs(Max),abs(Min))