class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def solve(arr,evod):
            ans = 1
            j = 0
            for i in range(len(arr)-1):
                if i%2 == evod:
                    if arr[i] <= arr[i+1]:
                        j=i+1
                else:
                    if arr[i] >= arr[i+1]:
                        j=i+1
                ans = max(ans,(i-j+2))
            return ans
          
        return max(solve(arr,0),solve(arr,1))