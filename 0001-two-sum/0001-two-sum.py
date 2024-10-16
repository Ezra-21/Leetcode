class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,val in enumerate(nums):
            value = target - val
            if value in dic:
                return dic[value],i
            dic[val] = i
        

            
        