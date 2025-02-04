class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashh = Counter(nums)
        for val,fre in hashh.items():
            if fre > len(nums)//2:
                return val

        
        