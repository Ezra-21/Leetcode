class Solution:
    def mySqrt(self, num: int) -> int:
        left = 0
        right = num
        while left <= right:
            mid = (left + right)//2
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                return mid
        return right