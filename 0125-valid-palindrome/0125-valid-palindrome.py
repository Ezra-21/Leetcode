class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter = ''.join( char for char in s if char.isalnum())
        letter = letter.lower()
       
        left,right = 0,len(letter)-1

        while left < right:
            if letter[left] != letter[right]:
                return False
            left += 1
            right -= 1
        return True
        