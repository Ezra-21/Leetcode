class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        summ_even = 0
        summ_odd = 0
        for i in range(len(nums)):
            if i%2==0:
                summ_even+=nums[i]
            else:
                summ_odd+=nums[i]
        prev_odd = 0
        prev_even = 0
        ans = 0

        for i in range(len(nums)):
            temp_odd,temp_even = summ_odd,summ_even
            if i%2==0:
                temp_even-=nums[i]
            else:
                temp_odd-=nums[i]

            new_even = temp_odd-prev_odd+prev_even
            new_odd = temp_even-prev_even+prev_odd

            if new_even == new_odd:
                ans+=1

            if i%2==0:
                prev_even+=nums[i]
            else:
                prev_odd+=nums[i]
        return ans
