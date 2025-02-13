class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right = 0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                option1 = (s[left+1:right+1] == s[left+1:right+1][::-1])
                option2 = (s[left:right] == s[left:right][::-1])

                return option1 or option2

            left+=1
            right-=1
        return True
        