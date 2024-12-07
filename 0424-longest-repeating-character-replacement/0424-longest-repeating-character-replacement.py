class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        res = 0
        for val in letter:
            res = max(res,self.solve(s,k,val))
        return res

    def solve(self,s,k,target):
        j = 0
        ans = 0
        count_non = 0
        for i in range(len(s)):
            if s[i]!=target:
                count_non+=1

            while count_non>k:
                if s[j]!=target:
                    count_non-=1
                j+=1


            ans = max(ans,i-j+1)
        return ans

