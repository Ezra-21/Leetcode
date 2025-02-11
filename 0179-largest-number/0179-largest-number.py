class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare_greater(num1,num2):
            if num1+num2 > num2+num1:
                return -1
            else:
                return 1

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        
        arranged = sorted(nums , key= cmp_to_key(compare_greater))

        return ''.join(arranged) if arranged[0]!='0' else '0'
        