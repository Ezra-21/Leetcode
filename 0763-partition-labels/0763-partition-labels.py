class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashh = {}
        for i in range(len(s)):
            hashh[s[i]] = i

        j = hashh[s[0]]
        k = 0
        ans = []
        for i in range(len(s)):
            j = max(j,hashh[s[i]])
            if i==j:
                ans.append(i-k+1)
                k = i+1

        return ans

        