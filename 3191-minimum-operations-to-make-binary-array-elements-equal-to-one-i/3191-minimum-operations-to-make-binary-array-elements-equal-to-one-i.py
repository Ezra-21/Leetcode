class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i+2<len(nums):
                    for j in range(i,i+3):
                        nums[j] = abs(nums[j]-1)
                    ans+=1
                else:
                    return -1
        return(ans)

            
            

        

        