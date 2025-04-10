class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums)==0:
            return 0
        n = len(nums)
        arr = [0]*(n+1)
        i = 0
        for j,(s,e,c) in enumerate(queries):
            if i>e:
                continue
            s = max(s,i)
            arr[s]+=c
            arr[e+1]-=c

            while i<len(nums) and arr[i]>=nums[i]:
                i+=1
                if i==len(nums):
                    return j+1
                arr[i]+=arr[i-1]

        return -1

