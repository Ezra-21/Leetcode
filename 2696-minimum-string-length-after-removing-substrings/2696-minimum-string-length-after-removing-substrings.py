class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        arr = list(s)
        i,j = 0,1
        while j<n:
            target = arr[i] + arr[j]
            if target == "CD" or target == "AB":
                arr.pop(i)
                arr.pop(i)
                if i != 0:
                    i-=1
                    j-=1
            else:
                i+=1
                j+=1
            n = len(arr)

        return len(arr)

        