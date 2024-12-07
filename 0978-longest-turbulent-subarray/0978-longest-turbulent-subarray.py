class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        ans,prv = 1,''

        for r in range(1,len(arr)):
            if arr[r-1] > arr[r] and prv != '>':
                ans = max(ans,(r-l+1))
                prv = '>'
            elif arr[r-1] < arr[r] and prv != '<':
                ans = max(ans,(r-l+1))
                prv = '<'
            elif arr[r-1] == arr[r]:
                l = r
                prev = '='
            else:
                l = r-1

        return ans

