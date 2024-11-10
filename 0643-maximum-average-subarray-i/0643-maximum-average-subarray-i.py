class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        ans = sum(nums[:k])
        for i in range(k,len(nums)):
            summ = summ - nums[i-k] + nums[i]
            ans = max(ans,summ)
        return ans/k
        