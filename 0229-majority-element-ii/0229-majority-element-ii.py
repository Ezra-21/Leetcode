class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashh = Counter(nums)
        ans = []
        for key,value in hashh.items():
            if value>n//3:
                ans.append(key)

        return ans

        