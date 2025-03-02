class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
            if nums[i]!=0:
                ans.append(nums[i])

            if i==n-2 and nums[i+1]!=0:
                ans.append(nums[i+1])
        m = len(ans)
        for _ in range(n-m):
            ans.append(0)

        return ans