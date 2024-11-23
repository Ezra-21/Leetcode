class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_sum = sum(nums)
        left_sum = 0
        res = []

        for i in range(n):
            res.append(abs(right_sum-(nums[i]*(n-i)))+abs(left_sum - (nums[i]*(i))))
            left_sum += nums[i]
            right_sum -= nums[i]

        return res


        