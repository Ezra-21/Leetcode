class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashh = Counter() 

        for a in nums1:
            for b in nums2:
                hashh[a+b]+=1

        res = 0

        for a in nums3:
            for b in nums4:
                target = -(a+b)
                if target in hashh:
                    res+=hashh[target]


        return res


