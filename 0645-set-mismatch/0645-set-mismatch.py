class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        miss,n = 0,len(nums)
        hashh = Counter(nums)
        for val,fre in hashh.items():
            if fre>1:
                miss = val
                break
        target = n*(n+1)//2
        summ = sum(nums)
        rem = target-summ
        print(rem)
        return miss,miss+rem