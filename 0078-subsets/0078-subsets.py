class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        total = 1<<len(nums)
        for i in range(total):
            temp = []
            for j in range(len(nums)):
                if i & (1<<j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans



