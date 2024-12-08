class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        temp = float('inf')
        n = len(cardPoints)
        summ = 0
        j = 0
        for i in range(n):
            summ += cardPoints[i]

            if i-j+1 > n-k:
                summ -= cardPoints[j]
                j+=1

            if i-j+1 == n-k:
                temp = min(temp,summ)
        return sum(cardPoints) - temp

