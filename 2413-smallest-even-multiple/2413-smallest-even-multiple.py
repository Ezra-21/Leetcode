class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        j = n
        while j%2 != 0 or j%n != 0:
            j+=1
        return j