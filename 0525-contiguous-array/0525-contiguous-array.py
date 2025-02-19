class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashh = {0:-1}
        prefix = 0
        max_len = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix not in hashh:
                hashh[prefix] = i
            else:
                max_len = max(max_len,i-hashh[prefix]+1)

        return max_len

        