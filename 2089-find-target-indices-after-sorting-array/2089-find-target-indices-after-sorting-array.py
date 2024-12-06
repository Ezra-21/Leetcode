class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i,val in enumerate(nums):
            if val == target:
                ans.append(i)

        return ans