class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs[0])):
            check = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i]!= check:
                    return ''.join(res)
            res.append(check)
        return ''.join(res)