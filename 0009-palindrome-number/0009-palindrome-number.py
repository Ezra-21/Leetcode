class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x == 0:
            return True

        length = math.floor(math.log10(x))+1
        if length == 1:
            return True
        place = 10**(length-1)

        while place>1:
            if x//place != x%10:
                return False
            x %= place
            x //= 10

            place //= 100
        return True
        