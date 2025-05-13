class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        new = x^y
        return new.bit_count()