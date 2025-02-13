class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashh = Counter()
        Max = 0
        j = 0
        for i in range(len(s)):
            if s[i] in hashh:
                while s[j]!=s[i]:
                    del hashh[s[j]]
                    j+=1
                hashh[s[j]]-=1
                j+=1

            hashh[s[i]]+=1
        
            Max = max(Max,i-j+1)

        return Max


                    

        