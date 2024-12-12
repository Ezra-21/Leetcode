class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        check = n//2
        hashh = Counter(nums)
        for num in set(nums):
            if hashh[num]>check:
                return num
        