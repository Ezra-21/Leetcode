class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        if n>m: return False
        dic_s1 = {}
        dic_s2 = {}

        for val in s1:
            if val not in dic_s1:
                dic_s1[val] = 0
            dic_s1[val] += 1

        for i in range(n):
            if s2[i] not in dic_s2:
                dic_s2[s2[i]] = 0
            dic_s2[s2[i]] += 1
        
        for i in range(n,m):
            if dic_s1 == dic_s2:
                return True

            dic_s2[s2[i-n]] -= 1
            if dic_s2[s2[i-n]] == 0:
                del dic_s2[s2[i-n]]
            
            if s2[i] not in dic_s2:
                dic_s2[s2[i]] = 0
            dic_s2[s2[i]] += 1
        
        
        return dic_s1 == dic_s2