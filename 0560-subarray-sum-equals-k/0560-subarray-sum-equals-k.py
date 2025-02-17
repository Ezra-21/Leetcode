class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashh = {0:1}
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            prefix+=nums[i]
            ans+=hashh.get(prefix-k,0)
            hashh[prefix]=hashh.get(prefix,0)+1

        return ans



        