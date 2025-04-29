class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        hashh = Counter(nums)
        nums.sort()
        ans,fre = -1,0
        for val in nums:
            if val%2==0 and hashh[val]>fre:
                ans = val
                fre = hashh[val]
        return ans

