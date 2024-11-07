class Solution:
    def largestMerge(self, arr: str, arr1: str) -> str:
        n,m = len(arr),len(arr1)
        ans = []
        i,j = 0,0
        while i<n and j<m:
            if arr[i:] > arr1[j:]:
                ans.append(arr[i])
                i += 1
            else:
                ans.append(arr1[j])
                j += 1
            
        ans.append(arr[i:])
        ans.append(arr1[j:])
        return ''.join(ans)
                    




        