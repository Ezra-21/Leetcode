class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashh = Counter(nums)
        for _,fre in hashh.items():
            if fre%2!=0:
                return False
        return True
        