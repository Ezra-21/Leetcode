class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def operation(answerKey,k,truth):
            ans = 0
            j = 0
            for i in range(len(answerKey)):
                if answerKey[i] != truth:
                    k-=1

                while k<0:
                    if answerKey[j] != truth:
                        k+=1
                    j+=1

                ans = max(ans,i-j+1)

            return ans
        
        return max(operation(answerKey,k,'T'),operation(answerKey,k,'F'))
