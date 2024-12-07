class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left,right = 0,int(math.sqrt(c))
        while left<=right:
            target = left**2+right**2
            if target == c:
                return True
            elif target < c:
                left+=1
            else:
                right-=1
        return False
