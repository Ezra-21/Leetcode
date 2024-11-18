class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_arr = []
        for i in range(len(nums)):
            total = 0
            for j in range(i,len(nums)):
                total += nums[j]
                sum_arr.append(total)
        sum_arr.sort()
        return sum(sum_arr[left-1:right])
