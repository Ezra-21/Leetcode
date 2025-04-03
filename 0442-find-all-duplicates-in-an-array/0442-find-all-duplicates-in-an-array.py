class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for val in nums:
            idx = abs(val)-1
            if nums[idx]<0:
                ans.append(abs(val))
            else:
                nums[idx]*=-1
        return ans
        







