class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2==1:
            return []
        original = []
        hashh = {}
        for val in changed:
            if val not in hashh:
                hashh[val] = 0
            hashh[val] += 1
        changed.sort()
        for num in changed:
            if num in hashh and num*2 in hashh:
                if num==num*2:
                    if hashh[num]>1:
                        original.append(num)
                        hashh[num]-=2
                    
                else:
                    original.append(num)
                    hashh[num*2]-=1
                    hashh[num]-=1
                    if hashh[num*2]==0:
                        del hashh[num*2]
                    if hashh[num]==0:
                        del hashh[num]
           
            
        return original if len(original)==n//2 else []
            

        