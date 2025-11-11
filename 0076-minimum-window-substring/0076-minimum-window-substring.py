class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if m > n:
            return ''
        hashh_t = Counter(t)
        hashh_s = Counter()
        
        length, ans = float('inf'), ''
        check= 0
        l = 0
        
        
        for i in range(n):   
            hashh_s[s[i]] +=1
            if s[i] in hashh_t and hashh_s[s[i]] == hashh_t[s[i]]:
                check += 1
            
            while check == len(hashh_t):
                if length > i-l + 1:
                    length = i - l + 1
                    ans = s[l:i+1]

                hashh_s[s[l]]-=1
                if s[l] in hashh_t and hashh_s[s[l]]<hashh_t[s[l]]:
                    check -= 1  
                l += 1

        return ans
