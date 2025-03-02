class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pref,post = 1,1
        maxi = float('-inf')
        for i in range(n):
            if pref == 0:
                pref = 1
            if post == 0:
                post = 1

            pref*=nums[i]
            post*=nums[n-i-1]

            maxi = max(maxi,max(pref,post))

        return maxi