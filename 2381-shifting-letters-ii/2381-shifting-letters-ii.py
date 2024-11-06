class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0]*(n+1)
        for start,end,dirc in shifts:
            if dirc == 1:
                arr[start] += 1
                arr[end+1] -= 1
            else:
                arr[start] -= 1
                arr[end+1] += 1
        
        for i in range(1,n):
            arr[i] += arr[i-1]

        ans = []

        for i in range(n):
            val = chr((ord(s[i])-ord('a') + arr[i])%26 + ord('a'))
            ans.append(val)

        return ''.join(ans)
