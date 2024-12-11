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
        count = 1
        for i in range(len(s)):
            for j in range(i+count,len(s)):
                found = palindrom(s[i:j+1])
                if found:
                    if count<j-i+1:
                        ans = s[i:j+1]
                        count = j-i+1

        return ans
        