class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            hashh = Counter()
            for j in range(i,len(s)):
                hashh[s[j]] += 1
                if hashh[s[j]] == k:
                    ans+=(len(s)-j)
                    break
        return ans

        