class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashh = Counter(nums)
        ans = []
        for val,fre in hashh.items():
            if fre>1:
                ans.append(val)

        return ans
        