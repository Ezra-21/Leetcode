class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 0,x
        while left<=right:
            mid = (left+right)//2
            target = mid*mid
            if target == x:
                return mid
            elif target>x:
                right = mid-1
            else:
                left = mid+1

        return right
