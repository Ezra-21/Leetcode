class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashh = Counter(nums)
        for fre in hashh.values():
            if fre%2!=0:
                return False
        return True
        