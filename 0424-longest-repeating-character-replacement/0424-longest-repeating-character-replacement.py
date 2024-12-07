class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        for val in set(s):
            result = max(result,self.solve(s,k,val))
        return result


    def solve(self,s,k,target):
        ans,j = 0,0
        for i in range(len(s)):
            if s[i] != target:
                k-=1
            while k<0:
                if s[j] != target:
                    k+=1
                j+=1

                    
            ans = max(ans,i-j+1)
                

        return ans


        