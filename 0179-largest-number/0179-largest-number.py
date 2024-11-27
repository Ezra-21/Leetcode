class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(num1,num2):
            if num1+num2 > num2+num1:
                return -1
            else:
                return 1
        for i,val in enumerate(nums):
            nums[i] = str(val)

        sorted_arr = sorted(nums,key=cmp_to_key(comparator))
        ans = ''.join(sorted_arr)
        return '0' if ans[0] == '0' else ans

        