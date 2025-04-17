class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0
        result=[]
        for val in nums:
            current_sum += val
            result.append(current_sum)
            
        return(result)
