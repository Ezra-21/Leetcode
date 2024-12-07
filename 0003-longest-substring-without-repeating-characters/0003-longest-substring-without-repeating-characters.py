class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        j,ans = 0, 0
        for i,val in enumerate(s):
            if val not in sett:
                sett.add(val)
            else:
                while s[j] != val:
                    sett.remove(s[j])
                    j+=1
                sett.remove(s[j])
                j+=1
                sett.add(val)

            ans = max(ans,i-j+1)
        
        return ans
