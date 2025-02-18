class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0:-1}
        count = 0
        max_len = 0


        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            
            if count in map:
                max_len = max(max_len, i - map[count])
            else:
                map[count] = i
        return max_len

                