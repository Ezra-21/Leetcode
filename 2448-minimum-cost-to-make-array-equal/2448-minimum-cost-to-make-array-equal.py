class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        pair = sorted(zip(nums,costs))
        summ = sum(costs)
        target = 0
        prefix = 0
        for num,cost in pair:
            prefix+=cost
            if prefix>summ//2:
                target = num
                break
        print(target)
        ans = 0
        for num,cost in pair:
            ans+=abs(target-num)*cost

        return ans

