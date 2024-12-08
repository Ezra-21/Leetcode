class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        ans = 0
        for i in range(1,len(prices)):
            if prices[i]+1==prices[i-1]:
                count+=1
            else:
                ans+=count*(count+1)//2
                count = 1
            if i == len(prices)-1:
                ans+=count*(count+1)//2
        return 1 if ans ==0 else ans



        