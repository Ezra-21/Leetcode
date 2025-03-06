class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_r,count_l = 0,0
        count = 0
        for c in s:
            if c == 'R':
                count_r+=1
            else:
                count_l+=1
            
            if count_r == count_l:
                count+=1
        return count
        