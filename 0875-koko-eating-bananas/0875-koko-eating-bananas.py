class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        total = sum(piles)
        ress = max(piles)
        while left<=right:
            mid = (left+right)//2
            
            res = sum(math.ceil(pile/mid) for pile in piles)

            if res>h:
                left = mid+1
            else:
                ress = mid
                right = mid-1

        return ress
 