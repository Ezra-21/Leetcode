class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrom(ss):
            left,right = 0,len(ss)-1
            while left<=right:
                if ss[left]!=ss[right]:
                    return False
                left+=1
                right-=1
            return True
        ans = s[0]
        for i in range(len(s)):
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if palindrom(substring) and len(substring)>len(ans):
                    ans = substring

        return ans
        