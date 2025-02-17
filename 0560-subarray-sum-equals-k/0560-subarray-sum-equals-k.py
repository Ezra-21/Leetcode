class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashh = {0:1}
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix-k in hashh:
                ans+=hashh[prefix-k]
            if prefix not in hashh:
                hashh[prefix] = 0
            hashh[prefix]+=1

        return ans



        