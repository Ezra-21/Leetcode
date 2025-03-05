class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i<len(flowerbed):
            if flowerbed[i]==1:
                i+=2
            else:
                if i<len(flowerbed)-1:
                    if flowerbed[i+1] == 0:
                        n-=1
                        i+=2
                    else:
                        i+=3
                else:
                    if i-1>=0 :
                        if flowerbed[i-1]==0:
                            n-=1
                    else:
                        n-=1
                    i+=1
            if n<=0:
                return True
        return n == 0

