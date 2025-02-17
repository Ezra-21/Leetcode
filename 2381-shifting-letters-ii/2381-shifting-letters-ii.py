class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]*len(s)

        for start,end,change in shifts:
            if change==0:
                change = -1
            arr[start]+=change
            if end!=len(s)-1:
                arr[end+1]-=change

        for i in range(1,len(s)):
            arr[i]+=arr[i-1]

        ans = []
        for i,ch in enumerate(s):
            new = chr(((ord(ch)-ord('a'))+arr[i])%26 + ord('a'))
            ans.append(new)

        return ''.join(ans)