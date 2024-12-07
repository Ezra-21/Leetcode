class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = -1
        for right in range(1,len(nums)):
            if left==-1 and nums[right]==nums[right-1]:
                left = right-1
            elif left!=-1 and nums[right]!=nums[left]:
                left+=1
                nums[left] = nums[right]
                
        return len(nums) if left+1 == 0 else left+1
        

        