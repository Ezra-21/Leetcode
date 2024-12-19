class Solution:
    def minChanges(self, s: str) -> int:
        i,j = 0,1
        cnt = 0
        while j<len(s):
            if s[i]!=s[j]:
                cnt+=1
            i+=1
            j+=1
        return cnt

        