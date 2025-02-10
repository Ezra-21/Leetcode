class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 , count_1 , count_2 = 0,0,0
        for val in nums:
            if val==0:
                count_0+=1
            elif val==1:
                count_1+=1
            else:
                count_2+=1
        i = 0
        for _ in range(count_0):
            nums[i] = 0
            i+=1

        for _ in range(count_1):
            nums[i] = 1
            i+=1

        for _ in range(count_2):
            nums[i] = 2
            i+=1

        return nums




