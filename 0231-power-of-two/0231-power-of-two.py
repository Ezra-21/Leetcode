class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return True if n&(n-1) == 0 else False
        