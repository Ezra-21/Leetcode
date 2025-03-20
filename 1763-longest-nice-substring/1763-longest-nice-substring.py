class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(sub):
            for char in sub:
                if char.lower() not in sub or char.upper() not in sub:
                    return False
            return True


        ans = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub = s[i:j+1]
                if solve(sub) and len(sub)>len(ans):
                    ans = sub
        return ans

                