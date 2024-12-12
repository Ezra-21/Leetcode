class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        for num in set(nums):
            if num-1 not in sett:
                longer = 1
                while num+1 in sett:
                    longer+=1
                    num +=1
                ans = max(ans,longer)


        return ans