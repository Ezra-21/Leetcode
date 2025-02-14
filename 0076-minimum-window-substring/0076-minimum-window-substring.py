class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(hashh1,hashh2):
            for val,fre in hashh2.items():
                if hashh1[val]<fre:
                    return False

            return True

        n,m = len(s),len(t)

        if m>n:
            return ''
        hashh_t = Counter(t)
        hashh_include = Counter()
        length,index = float('inf'),[]
        j = 0
        for i in range(n):
            hashh_include[s[i]]+=1
            while (i-j+1)>=len(t) and check(hashh_include,hashh_t):
                if length>(i-j+1):
                    length = (i-j+1)
                    index = [j,i]
                hashh_include[s[j]]-=1
                j+=1

        return s[index[0]:index[1]+1] if index else ''
            
        