class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        s = set(nums)
        longest = 1

        for r in range(len(nums)):
            if nums[r] - 1 not in s:
                num = nums[r]
                cnt = 0
                while num in s:
                    cnt += 1
                    num += 1
                longest = max(longest, cnt)

        return longest
