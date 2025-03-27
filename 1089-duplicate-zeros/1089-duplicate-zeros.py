class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ans = []
        i ,n = 0,len(arr)
        j = 0
        while j<n:
            if arr[i]==0:
                ans.append(0)
                j+1
            ans.append(arr[i])
            i+=1
            j+=1

        for i in range(n):
            arr[i] = ans[i]

        return ans

        

        

        

        