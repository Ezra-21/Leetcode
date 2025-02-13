class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Max,summ = float('-inf'),0
        left = 0
        for i in range(len(nums)):
            summ += nums[i]

            if i-left >= k:
                summ-=nums[left]
                left+=1

            if i-left == k-1:
                Max = max(Max,summ)
            

        return Max/k

        