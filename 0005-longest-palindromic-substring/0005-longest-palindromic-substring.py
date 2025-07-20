class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkpal(word):
            i,j = 0,len(word)-1
            while i<=j:
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True

        ans = ''
        for i in range(len(s)):
            for j in range(i+len(ans),len(s)):
                substring = s[i:j+1]
                if checkpal(substring) and len(substring)>len(ans):
                    ans = substring

        return ans

