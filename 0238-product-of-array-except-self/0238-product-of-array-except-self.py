class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_0 = nums.count(0)
        total = 1
        if count_0 <=1:
            for val in nums:
                if val != 0:
                    total *= val
        ans = []
        for num in nums:
            if count_0 == 0:
                ans.append(total//num)
            elif count_0 == 1:
                if num == 0:
                    ans.append(total)
                else:
                    ans.append(0)
            else:
                ans.append(0)

        return ans


                