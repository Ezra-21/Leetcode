class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = nums.copy()
        arr.sort()
        left,right = 0,len(arr)-1
        l,r = True,True
        while left<right:
            if l and nums[left]!=arr[left]:
                l = False
            if r and nums[right]!=arr[right]:
                r = False
            
            if l:
                left+=1
            if r:
                right-=1
            if not l and not r:
                break

        ans = right-left
        return ans+1 if ans!=0 else 0
                
                
        