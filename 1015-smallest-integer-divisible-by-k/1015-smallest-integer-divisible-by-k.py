class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        num = 1
        lenn = 1

        while k%2!=0 and k%5!=0 and lenn<=k:
            if num%k == 0:
                return lenn
            num = num*10+ 1
            lenn+=1
        return -1
            
        