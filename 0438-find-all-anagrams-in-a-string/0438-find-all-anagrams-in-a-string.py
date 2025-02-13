class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m = len(s),len(p)
        hashh_p = Counter(p)
        hashh_anag = Counter(s[:m-1])
        ans = []
        l = 0
        for i in range(m-1,n):
            hashh_anag[s[i]]+=1

            if hashh_p == hashh_anag:
                ans.append(l)
            
            hashh_anag[s[l]]-=1
            if hashh_anag[s[l]] == 0:
                del hashh_anag[s[l]]
            l+=1

        return ans
            
        