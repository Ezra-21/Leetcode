class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        hashh = Counter(tiles)

        def backtrack():
            res = 0

            for c in hashh:
                if hashh[c]>0:
                    hashh[c]-=1
                    res+=1
                    res+=backtrack()
                    hashh[c]+=1

            return res
            

        return backtrack()
        