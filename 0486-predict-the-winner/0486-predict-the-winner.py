class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def solve(l,r):
            if l==r:
                return nums[l]

            left = nums[l] - solve(l+1,r)
            right = nums[r] - solve(l,r-1)

            return max(left,right)

        l,r = 0,len(nums)-1
        return solve(l,r)>=0