class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            step = nums[i]
            if step>0:
                ans.append(nums[(i+step)%n])
            elif step<0:
                ans.append(nums[(i+step)%n])
            else:
                ans.append(nums[i])

        return ans


        