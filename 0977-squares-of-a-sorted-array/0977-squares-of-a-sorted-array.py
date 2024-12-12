class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i,num in enumerate(nums):
            nums[i] = num*num
        ans = []
        left,right = 0,len(nums)-1
        while left<=right:
            if nums[left]<nums[right]:
                ans.append(nums[right])
                right-=1
            else:
                ans.append(nums[left])
                left+=1

        return ans[::-1]

