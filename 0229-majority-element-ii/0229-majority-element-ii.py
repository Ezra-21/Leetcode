class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashh = Counter(nums)
        ans = []
        for val,fre in hashh.items():
            if fre>len(nums)//3:
                ans.append(val)

        return ans
        