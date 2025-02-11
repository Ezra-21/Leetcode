class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        
        nums.sort(key=lambda x:x*9 , reverse = True)

        return ''.join(nums) if nums[0]!='0' else '0'
        