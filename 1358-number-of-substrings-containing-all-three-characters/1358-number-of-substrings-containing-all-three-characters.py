class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashh = Counter()
        max_substring = 0
        j = 0
        for i,char in enumerate(s):
            hashh[char] += 1

            while len(hashh) == 3:
                max_substring += len(s) - i
                hashh[s[j]]-=1
                if hashh[s[j]] == 0:
                    del hashh[s[j]]

                j+=1


        return max_substring


        