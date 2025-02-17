class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashh = {0:1}
        ans = 0
        prefix = 0
        for num in nums:
            prefix+=num
            remain = prefix%k
            if remain in hashh:
                ans+=hashh[remain]

            hashh[remain] = hashh.get(remain,0)+1

        return ans

