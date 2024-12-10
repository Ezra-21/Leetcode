class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashh = {}
        for val in s:
            if val not in hashh:
                hashh[val] = 0
            hashh[val] += 1

        for i,char in enumerate(s):
            if hashh[char] == 1:
                return i
            
        return -1

        
        