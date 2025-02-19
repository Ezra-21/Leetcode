class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashh = {0:1}
        ans = 0
        prefix = 0
        for val in nums:
            prefix+=val
            target = prefix-goal
            if target in hashh:
                ans+=hashh[target]

            if prefix not in hashh:
                hashh[prefix] = 0
            hashh[prefix]+=1
        return ans
        