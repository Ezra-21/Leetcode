class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def check(hashh):
            see = ['a','b','c']
            for val in see:
                if val not in hashh or hashh[val]<1:
                    return False
            return True

        hashh = {}
        ans,n = 0,len(s)
        j = 0
        for i in range(n):
            hashh[s[i]] = hashh.get(s[i],0)+1
            while check(hashh):
                ans+=(n-i)
                hashh[s[j]]-=1
                j+=1

        return ans
