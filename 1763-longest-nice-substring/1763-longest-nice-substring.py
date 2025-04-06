class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def nice_substring(substring):
            for char in substring:
                if char.lower() not in substring or char.upper() not in substring:
                    return False
            return True


        longest_subtring = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if nice_substring(substring) and len(substring)>len(longest_subtring):
                    longest_subtring = substring
        return longest_subtring

                