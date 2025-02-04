class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashh = Counter(nums)
        return any(hashh[val]>=2 for val in hashh)
        