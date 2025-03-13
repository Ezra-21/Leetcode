class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        summ = 0
        j = 0

        for i,(s,e,val) in enumerate(queries):
            while j<n:
                if nums[j]<=summ+prefix[j]:
                    summ+=prefix[j]
                    j+=1
                else:
                    break
                if j==n:
                    return i

            if e<j:
                continue
            s = max(j,s)
            prefix[s] += val
            prefix[e+1] -= val

            
        return -1


