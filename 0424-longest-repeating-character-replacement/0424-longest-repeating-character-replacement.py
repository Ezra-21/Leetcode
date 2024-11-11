class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        for val in set(s):
            result = max(result, self.solve(s, k, val))
        return result

    def solve(self, s, k, target):
        ans, j = 0, 0  # Initialize answer and left pointer
        current_k = k  # Store original k value for each target character

        for i in range(len(s)):
            if s[i] != target:
                if current_k > 0:
                    current_k -= 1
                else:
                    # Move left pointer to make room for replacements within limit
                    while s[j] == target:
                        j += 1
                    j += 1  # Move past the first non-target character to reduce window size

            # Update maximum window length
            ans = max(ans, i - j + 1)

        return ans
