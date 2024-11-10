class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        i,j,ans = 0,0,0
        while i < len(s):
            if s[i] not in sett:
                sett.add(s[i])
                i+=1
            else:
                while s[j] != s[i]:
                    sett.remove(s[j])
                    j+=1
                sett.remove(s[j])
                j+=1
            ans = max(i-j,ans)

        return ans
                