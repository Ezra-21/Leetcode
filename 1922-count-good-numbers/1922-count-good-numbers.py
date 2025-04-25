class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_pos = math.ceil(n/2)
        odd_pos = n-even_pos
        return (pow(5,even_pos,MOD)*pow(4,odd_pos,MOD))%MOD