class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        miss,n = 0,len(nums)
        hashh = Counter(nums)
        for val,fre in hashh.items():
            if fre>1:
                miss = val
                break
        target,summ = n*(n+1)//2,sum(nums)
        return miss,miss+(target-summ)