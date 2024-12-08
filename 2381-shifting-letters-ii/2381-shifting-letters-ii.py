class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0]*(n+1)

        for start,end,inc in shifts:
            rr = 1 if inc==1 else -1
            arr[start] += rr
            arr[end+1] -= rr

        for i in range(1,n+1):
            arr[i] += arr[i-1]

        ans = []

        for i in range(n):
            char = chr(((ord(s[i])-ord('a'))+(arr[i]%26))%26+ord('a'))
            ans.append(char)

        return "".join(ans)