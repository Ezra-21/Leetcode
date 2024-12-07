class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans,summ = 0,0
        j = 0
        for i in range(len(s)):
            summ += (abs(ord(s[i])-ord(t[i])))

            while summ>maxCost:
                summ -= (abs(ord(s[j])-ord(t[j])))
                j+=1
            
            ans = max(ans,i-j+1)
        return ans
