class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count_0,count_1 = 0,0
        ans_1 , ans_0 = 0,0
        for num in s:
            if num=='1':
                count_1+=1
                count_0 = 0
                ans_1 = max(ans_1,count_1)
            else:
                count_0+=1
                count_1 = 0
                ans_0 = max(ans_0,count_0)
        print(ans_1,ans_0)
        return ans_1>ans_0