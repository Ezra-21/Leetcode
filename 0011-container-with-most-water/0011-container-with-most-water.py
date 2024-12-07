class Solution:
    def maxArea(self, arr: List[int]) -> int:
        ans = 0
        left,right = 0,len(arr)-1
        while left<right:
            ans = max(ans,(right-left)*min(arr[left],arr[right]))
            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
        return ans

        
            

        