class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        ans = 0
        def operator(num):
            return num*(num+1)//2

        for i in range(1,len(prices)):
            if prices[i]+1==prices[i-1]:
                count+=1
            else:
                ans+=operator(count)
                count = 1
            if i == len(prices)-1:
                ans+=operator(count)

        return 1 if ans ==0 else ans



        