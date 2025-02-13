class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        Max = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k-=1

            while k<0:
                if nums[j] == 0:
                    k+=1
                j+=1

            Max = max(Max,i-j+1)
        return Max