class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashh = {'a':-1,'b':-1,'c':-1}
        max_substring = 0

        for i,char in enumerate(s):
            hashh[char] = i

            if hashh['a']!=-1 and hashh['b']!=-1 and hashh['b']!=-1:
                max_substring += min(hashh.values())+1

        return max_substring


        