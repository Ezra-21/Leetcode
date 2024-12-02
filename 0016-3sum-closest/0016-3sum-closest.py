class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sum1 = float('-inf')
        sum2 = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left,right = i+1,len(nums)-1
            while left<right:
                summation = nums[i]+nums[left]+nums[right]
                
                if summation < target:
                    sum1 = max(sum1,summation)
                    left += 1
                elif summation > target:
                    sum2 = min(sum2,summation)
                    right -= 1
                else:
                    return target
        return sum1 if (target-sum1) < (sum2-target) else sum2
        