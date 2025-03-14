class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(l,r):
            if dp[l][r]!=-1:
                return dp[l][r]

            if l==r:
                return nums[l]

            left = nums[l] - solve(l+1,r)
            right = nums[r] - solve(l,r-1)
            dp[l][r] = max(left,right)

            return dp[l][r]
        
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]
        return solve(0,n-1) >= 0



