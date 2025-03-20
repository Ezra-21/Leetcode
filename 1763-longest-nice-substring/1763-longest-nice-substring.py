class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        def solve(sub):
            if len(sub) < 2:
                return ""

            unique = set(sub)
            for i, char in enumerate(sub):
                if char.lower() not in unique or char.upper() not in unique:
                    left = solve(sub[:i])
                    right = solve(sub[i + 1:])
                    return left if len(left) >= len(right) else right

            return sub  

        return solve(s)
