class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hold = -1
        for i,val in enumerate(nums):
            if val==0:
                hold = i
                break
        if hold == -1:
            return 0

        ans = 0
        for i in range(hold,len(nums)):
            if nums[i] == 0:
                if i+2<len(nums):
                    for j in range(i,i+3):
                        nums[j] = abs(nums[j]-1)
                    ans+=1
                else:
                    return -1

        return(ans)

            
            

        

        