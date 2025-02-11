class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        start = len(piles)//3
        return sum(piles[start::2])
        