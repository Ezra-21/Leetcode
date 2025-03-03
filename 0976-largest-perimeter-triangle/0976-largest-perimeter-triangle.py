class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            target = nums[i+1]+nums[i+2]
            if target>nums[i]:
                return target+nums[i]

        return 0