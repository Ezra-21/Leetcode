class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums)-x
        summ = 0
        left=0
        ans = -1
        for right in range(n):
            summ+=nums[right]
            while summ>target and left<right:
                summ-=nums[left]
                left+=1
            if summ==target:
                ans = max(ans,right-left+1)
            
        

        return n-ans if ans!=-1 else -1


