class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashh = Counter()
        for cost in bills:
            hashh[cost]+=1
            if cost == 10:
                if 5 in hashh:
                    hashh[5]-=1
                    if hashh[5] == 0:
                        del hashh[5]
                else:
                    return False
                
            elif cost == 20:
                if 5 in hashh and 10 in hashh:
                    hashh[5]-=1
                    hashh[10]-=1
                    if hashh[5] == 0:
                        del hashh[5]
                    if hashh[10] == 0:
                        del hashh[10]
                elif hashh[5]>=3:
                    hashh[5]-=3
                    if hashh[5] == 0:
                        del hashh[5]
                else:
                    return False
        return True