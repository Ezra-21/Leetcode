class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashh = {0:-1}
        prefix = 0
        max_len = 0
        for i in range(len(nums)):
            prefix += 1 if nums[i]==1 else -1
            if prefix not in hashh:
                hashh[prefix] = i
            else:
                max_len = max(max_len,i-hashh[prefix])

        return max_len

        