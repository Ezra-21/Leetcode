class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        hashh_s1 = Counter()
        hashh_s2 = Counter()

        for val in s1:
            hashh_s1[val]+=1

        j = 0
        for i,val in enumerate(s2):
            hashh_s2[val]+=1

            if (i-j+1) > n:
                hashh_s2[s2[j]]-=1
                if hashh_s2[s2[j]] == 0:
                    del hashh_s2[s2[j]]
                j+=1
                

            if (i-j+1) == n:
                if hashh_s1 == hashh_s2:
                    return True

        return False

