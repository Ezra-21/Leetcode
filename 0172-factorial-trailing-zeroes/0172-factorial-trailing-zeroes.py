class Solution:
    def trailingZeroes(self, n: int) -> int:
        count_0 = 0
        while n >= 5:
            n //= 5
            count_0 += n  # Count multiples of 5, 25, 125, etc.
        return count_0