class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        for start,end in requests:
            prefix[start]+=1
            prefix[end+1]-=1

        for i in range(1,n):
            prefix[i]+=prefix[i-1]
        nums.sort(reverse=True)
        prefix.sort(reverse=True)
        ans = 0
        for i in range(n):
            if prefix[i]==0:
                break
            ans+=(prefix[i]*nums[i])

        return ans%(10**9 + 7)


        
        