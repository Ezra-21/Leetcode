class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashh = Counter({0:1})
        summ = 0
        ans = 0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ - k in hashh:
                ans += hashh[summ-k]

            hashh[summ] += 1
        return ans