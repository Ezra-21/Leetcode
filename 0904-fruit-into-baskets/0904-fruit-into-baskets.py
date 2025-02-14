class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashh_collect = Counter()
        l = 0
        maxi = 0
        for i in range(len(fruits)):
            hashh_collect[fruits[i]]+=1
            while len(hashh_collect)>2:
                hashh_collect[fruits[l]]-=1
                if hashh_collect[fruits[l]] == 0:
                    del hashh_collect[fruits[l]]
                l+=1

            maxi = max(maxi,i-l+1)

        return maxi
        