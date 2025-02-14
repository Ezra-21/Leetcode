class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = list(s)
        idx = -1
        for i in range(len(s)):
            if s[i] == '1':
                idx = i
                break
        swap = 0
        if idx!=-1:
            for i in range(idx+1,len(s)):
                if s[i]!='1':
                    swap+=(i-idx)
                    idx+=1
        

        return swap