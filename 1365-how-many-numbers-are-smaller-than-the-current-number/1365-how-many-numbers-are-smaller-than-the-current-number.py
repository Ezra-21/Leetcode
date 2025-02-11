class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashh = {}
        arr = sorted(nums)
        for i,num in enumerate(arr):
            if num not in hashh:
                hashh[num] = i
        ans = []
        for num in nums:
            ans.append(hashh[num])

        return ans

        