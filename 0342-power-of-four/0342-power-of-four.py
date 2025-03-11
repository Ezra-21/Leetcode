class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        return (math.pow(n,1/4)).is_integer()