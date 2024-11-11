class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p,len_s = len(p),len(s)
        ans = []
        if len_p > len_s:
            return ans
        dic_s = {}
        dic_p = {}
        
        for val in p:
            if val not in dic_p:
                dic_p[val] = 0
            dic_p[val]+=1

        for i in range(len_p):
            if s[i] not in dic_s:
                dic_s[s[i]] = 0
            dic_s[s[i]]+=1
        
        for i in range(len_p,len_s):
            if dic_s == dic_p:
                ans.append(i-len_p)
            dic_s[s[i-len_p]] -= 1
            if dic_s[s[i-len_p]] == 0:
                del dic_s[s[i-len_p]]
            
            if s[i] not in dic_s:
                dic_s[s[i]] = 0
            dic_s[s[i]]+=1
        if dic_s == dic_p:
            ans.append(len_s-len_p)

        return ans
            
        
        