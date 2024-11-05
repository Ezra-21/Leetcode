class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        seen = set()
        i = 1
        check = 0
        while i<len(nums):
            if nums[i] == nums[i-1]:
                check = 1
                break
            i+=1
        if not check: return len(nums)

        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                seen.add(nums[j])
            else:
                if nums[j] not in seen:
                    seen.add(nums[j])
                    nums[i] , nums[j] = nums[j] , nums[i]
                    i += 1

        return i

        