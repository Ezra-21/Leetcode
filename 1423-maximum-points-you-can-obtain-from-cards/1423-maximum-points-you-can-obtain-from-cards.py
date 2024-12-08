class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_summ = sum(cardPoints[:k])
        right_summ = 0
        ans = left_summ
        for i in range(1,k+1):
            left_summ -= cardPoints[k-i]
            right_summ += cardPoints[-i]
            ans = max(ans,left_summ+right_summ)

        return ans