class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            exchange_bottle = numBottles//numExchange

            numBottles = exchange_bottle + (numBottles%numExchange)

            ans += exchange_bottle

        return ans
        