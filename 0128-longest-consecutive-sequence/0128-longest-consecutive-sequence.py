class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        ans = 0
        for num in sett:
            if num-1 not in sett:
                longer = 1
                while num+1 in sett:
                    longer+=1
                    num +=1
                ans = max(ans,longer)


        return ans