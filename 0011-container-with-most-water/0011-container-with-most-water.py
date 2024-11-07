class Solution:
    def maxArea(self, arr: List[int]) -> int:
        left,right = 0,len(arr)-1
        ans = 0
        while left < right:
            ans = max(ans,(right - left)*(min(arr[left],arr[right])))
            if arr[left] > arr[right]:
                right -= 1
            else:
                left += 1

        return ans
            

        