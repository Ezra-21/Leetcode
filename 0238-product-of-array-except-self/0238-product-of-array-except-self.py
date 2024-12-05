class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total = 1
        count_zero = 0

        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                total*=num
        print(total)
        ans = []
        for num in nums:
            if count_zero > 1:
                ans.append(0)
            elif count_zero == 1:
                if num == 0:
                    ans.append(total)
                else:
                    ans.append(0)
            else:
                ans.append(total//num)

        return ans
