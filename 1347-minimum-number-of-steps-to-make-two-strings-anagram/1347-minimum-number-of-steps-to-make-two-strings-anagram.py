class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashh_s = Counter(s)
        hashh_t = Counter(t)

        step = 0
        
        for val in t:
            print(hashh_t,hashh_t)
            print(val)
            if val in hashh_s:
                hashh_s[val]-=1
                hashh_t[val]-=1
                if hashh_s[val]==0:
                    del hashh_s[val]
                if hashh_t[val]==0:
                    del hashh_t[val]
                print(hashh_t,hashh_t)
                print(val)
            else:
                print(val)
                print(hashh_t,hashh_t)
                step+=hashh_t[val]
        print('j')
        return step
        