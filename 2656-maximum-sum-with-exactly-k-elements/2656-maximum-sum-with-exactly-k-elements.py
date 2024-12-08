class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        Max_num = nums[0]
        for val in nums:
            if val>Max_num:
                Max_num = val

        return Max_num*k+k*(k-1)//2

        