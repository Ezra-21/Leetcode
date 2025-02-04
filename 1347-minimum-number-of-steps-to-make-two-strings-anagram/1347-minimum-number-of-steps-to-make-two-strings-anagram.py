class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashh_s = Counter(s)
        hashh_t = Counter(t)

        step = 0
        
        for val in hashh_t:
            if val in hashh_s:
                if hashh_t[val]-hashh_s[val]>0:
                    step+= (hashh_t[val]-hashh_s[val])
               
            else:
                
                step+=hashh_t[val]
        
        return step
        