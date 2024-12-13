class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        ans = 0
        for num in unique:
            longest = 1
            
            if num-1 not in unique:
                while num+1 in unique:
                    longest+=1
                    num+=1
                ans = max(ans,longest)


        return ans
        