class Solution:#43%9=2
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashh = Counter({0:1})
        prefix = 0
        ans = 0
        for num in nums:
            prefix+=num
            remainder = prefix%k
            if remainder in hashh:
                ans+=hashh[remainder]

            hashh[remainder]+=1

        return ans


        
        