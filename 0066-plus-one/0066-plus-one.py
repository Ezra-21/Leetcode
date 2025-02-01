class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        remainder = 0
        digits[-1]+=1
        if digits[-1] == 10:
            remainder = 1
            digits[-1] = 0
        for i in range(length-2,-1,-1):
            digits[i] += remainder
            if digits[i] == 10:
                remainder = 1
                digits[i] = 0
            else:
                remainder = 0

        if remainder==1:
            digits = [1]+digits

        return digits



        


