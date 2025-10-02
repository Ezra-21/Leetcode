class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        ans = ''
        pos,check = True,True
        for i,ch in enumerate(s):
            if check and (ch=='-' or ch=='+'):
                if ch=='-':
                    pos = False
                check = False
            elif ch.isdigit() :
                ans+=ch
                check = False
            elif (ch == ' ' and check):
                continue
            else:
                break
        if ans:
            ans = int(ans)
            ans = ans if pos else -ans
            ans = max(INT_MIN, min(ans, INT_MAX))
        else:
            ans = 0
        return ans
           
                

            
            
