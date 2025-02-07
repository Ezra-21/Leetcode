class Solution: 
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashh = Counter()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pro = nums[i]*nums[j]
                hashh[pro]+=1

        ans = 0
        
        for value in hashh.values():

            ans+=4*((value*(value-1)))    

        return ans         
        