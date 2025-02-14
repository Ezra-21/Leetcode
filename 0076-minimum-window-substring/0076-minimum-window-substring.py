class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n,m = len(s),len(t)
        if m>n:
            return ''
        hashh_t = Counter(t)
        hashh_include = Counter()
        length,index = float('inf'),[]
        check = 0
        j = 0
        for i in range(n):
            hashh_include[s[i]]+=1
            while all(hashh_include[val]>=fre for val,fre in hashh_t.items()):
                if length>(i-j+1):
                    length = (i-j+1)
                    index = [j,i]
                if s[j] in hashh_t:
                    hashh_include[s[j]]-=1
                j+=1

        return s[index[0]:index[1]+1] if index else ''
            
        