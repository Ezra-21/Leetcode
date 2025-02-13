class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if abs(target - summ) < abs(target - ans):
                    ans = summ

                if summ > target:
                    right -= 1
                elif summ < target:
                    left += 1
                else:
                    return summ
        return ans
