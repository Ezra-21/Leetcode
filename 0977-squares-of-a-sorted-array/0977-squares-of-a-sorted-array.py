class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        left,right = 0,len(nums)-1
        while left<=right:
            if abs(nums[left])<(nums[right]):
                ans.append(nums[right]*nums[right])
                right-=1
            else:
                ans.append(nums[left]*nums[left])
                left+=1
        ans.reverse()

        return ans

