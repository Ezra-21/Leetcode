class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x == 0:
            return True

        length = math.floor(math.log10(x))+1
        place_value = 10**(length-1)

        while place_value>1:
            if (x//place_value)!=(x%10):
                return False
            x %= place_value
            x //= 10 

            place_value //= 100
        return True


