class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashh = Counter(s)
        ans = []
        for char in order:
            if char in hashh:
                ans.append(char*hashh[char])
                del hashh[char]

        for char,fre in hashh.items():
            ans.append(char*fre)

        return ''.join(ans)

        
        