class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashh = Counter(text)
        string = "balloon"
        ans = float('inf')
        for char in string:
            if char not in hashh:
                return 0
            if char=='l' or char=='o':
                ans = min(ans,hashh[char]//2)
            else:
                ans = min(ans,hashh[char])

        return ans

        