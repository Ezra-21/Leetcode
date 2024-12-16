class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        left,right = 0,len(arr)-1
        while left<right:
            if nums[left]==arr[left]:
                left+=1
            if nums[right]==arr[right]:
                right-=1
            if nums[left]!=arr[left] and nums[right]!=arr[right]:
                break


        return right-left+1 if right-left!=0 else 0
                
                
        