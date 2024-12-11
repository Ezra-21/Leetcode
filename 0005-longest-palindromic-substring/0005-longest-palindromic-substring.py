class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            n = len(s)
            l = int(n/2)
            if n == 1:
                return True
            if s[:l] == s[l+n%2:][::-1]:
                return True
            else:
                return False
        n = len(s)
        if isPalindrome(s):
            return s
        for i in range(n):
            substring_n = n - i
            for j in range(0, n - substring_n + 1):
                if isPalindrome(s[j:j+substring_n]):
                    return s[j:j+substring_n]
        return False