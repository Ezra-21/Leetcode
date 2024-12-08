class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        Max_num = nums[0]
        for val in nums:
            if val>Max_num:
                Max_num = val

        ans = 0

        for i in range(k):
            ans += Max_num+i

        return ans

        