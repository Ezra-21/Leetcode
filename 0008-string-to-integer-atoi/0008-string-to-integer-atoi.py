class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        ans = 0
        i = 0
        n = len(s)
        
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
            
        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1
        
        ans *= sign
        ans = max(-(2**31), min((2**31)-1, ans))
        return ans
