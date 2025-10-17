class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(i,collect):
            if len(collect) == len(digits):
                res.append(collect)
                return

            for ch in phone_map[digits[i]]:
                dfs(i+1,collect+ch)

        if digits:
            dfs(0,'')

        return res