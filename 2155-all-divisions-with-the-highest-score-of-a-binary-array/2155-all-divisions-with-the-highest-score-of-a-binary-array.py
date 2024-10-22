class Solution:
    def maxScoreIndices(self, arr: List[int]) -> List[int]:
        score = []
        ans = []
        count_1,count_0 = arr.count(1),0
        summ = count_1+count_0
        score.append(summ)
        for i in range(len(arr)):
            if arr[i] == 1:
                count_1 -= 1
            elif arr[i] == 0:
                count_0 += 1

            summ = count_1+count_0
            score.append(summ)
        Max = max(score)
        for i in range(len(score)):
            if score[i] == Max:
                ans.append(i)
        return ans
        

        