class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        hashh = {}
        hash1 = {}
        for char in string.ascii_lowercase:
            hashh[ord(char) - ord('a')] = char
        for char in string.ascii_lowercase:
            hash1[char] = ord(char) - ord('a')

        for a,b,c in shifts:
            res = ''
            for i in range(a,b+1):
                val = hash1[s[i]]
                if c == 0:
                    if val!=0:
                        val-=1
                    else:
                        val = 25
                else:
                    if val!=25:
                        val+=1
                    else:
                        val = 0
                res+=hashh[val]
            
            s = s[:a]+res+s[b+1:]
            
        return s
            