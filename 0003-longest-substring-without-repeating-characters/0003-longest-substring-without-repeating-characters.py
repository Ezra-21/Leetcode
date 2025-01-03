class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        j,ans = 0, 0
        for i,val in enumerate(s):
            if val in sett:
                while val in sett:
                    sett.remove(s[j])
                    j+=1
                
            sett.add(val)
            ans = max(ans,i-j+1)
        
        return ans
