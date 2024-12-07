class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashh = {}
        ans = 0
        start = 0
        for i in range(len(fruits)):
            if fruits[i] not in hashh:
                hashh[fruits[i]] = 0
            hashh[fruits[i]] += 1

            while len(hashh)>2:
                hashh[fruits[start]]-=1
                if hashh[fruits[start]] == 0:
                    del hashh[fruits[start]]
                start+=1

            
            ans = max(ans,i-start+1)
        return ans
            