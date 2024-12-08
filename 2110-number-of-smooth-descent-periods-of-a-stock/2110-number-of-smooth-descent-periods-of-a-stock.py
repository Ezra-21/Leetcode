class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prices.append(0)
        count = 1
        ans = 0
        for i in range(1,len(prices)):
            if prices[i]+1==prices[i-1]:
                count+=1
            else:
                ans+=count*(count+1)//2
                count = 1
        return 1 if ans ==0 else ans



        