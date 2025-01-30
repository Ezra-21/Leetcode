class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        str_num = str(x)
        l,r = 0,len(str_num)-1
        while l<r:
            if str_num[l]!=str_num[r]:
                return False
            l+=1
            r-=1
        return True
        