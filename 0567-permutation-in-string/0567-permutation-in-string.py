class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        hashh_s1 = Counter(s1)
        hashh_per = Counter(s2[:n-1])
        l = 0
        for i in range(n-1,m):
            hashh_per[s2[i]]+=1
            print(hashh_per)
            if hashh_s1 == hashh_per:
                return True

            hashh_per[s2[l]]-=1
            if hashh_per[s2[l]] == 0:
                del hashh_per[s2[l]]
            l+=1

        return False