class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        summ ,j = 0,0

        for i in range(n):
            while summ+prefix[i] < nums[i]:
                if j==len(queries):
                    return -1
                s,e,val = queries[j]
                j+=1
                if e<i:
                    continue
                s = max(s,i)
                prefix[s]+=val
                prefix[e+1]-=val

            summ+=prefix[i]

            
        
        return j


