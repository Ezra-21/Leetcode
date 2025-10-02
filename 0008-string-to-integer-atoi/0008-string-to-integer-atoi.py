class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31 
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        def recursion(index,number):
            if index == len(s) or not s[index].isdigit():
                return sign*number
            
            digit = int(s[index])
            number = number*10 + digit

            if number > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN
            
            return recursion(index+1 , number)

        
        return recursion(0,0)