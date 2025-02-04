class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthest = sum(accounts[0])
        for i in range(1,len(accounts)):
            wealthest = max(sum(accounts[i]),wealthest)

        return wealthest
            

        