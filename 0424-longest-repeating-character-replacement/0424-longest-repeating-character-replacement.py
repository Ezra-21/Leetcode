class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def operation(s,k,char):
            max_length = 0
            j = 0
            for i in range(len(s)):
                if s[i] != char:
                    k-=1
                    
                while k<0:
                    if s[j] != char:
                        k+=1
                    j+=1
                    
                max_length = max(max_length,i-j+1)
            return max_length
                
        
        unique = set(s)
        ans = 0
        for char in unique:
            ans = max(ans,operation(s,k,char))
        return ans
            

