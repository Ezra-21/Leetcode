class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        hashh = {'I' : 1,'V' : 5,'X'  : 10,'L' : 50,'C' : 100,'D' :  500,'M' : 1000}
        check = {'I':['V','X'],'X':['L','C'],'C':['D','M']}
        ans = 0
        i = 0
        while i<n:
            if i+1<n and s[i] in check:
                if s[i+1]==check[s[i]][0]:
                    ans += (hashh[check[s[i]][0]]-hashh[s[i]])
                    i+=2
                    continue
                elif s[i+1]==check[s[i]][1]:
                    ans += (hashh[check[s[i]][1]]-hashh[s[i]])
                    i+=2
                    continue
            ans += hashh[s[i]]
            i+=1
        return ans





        