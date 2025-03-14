class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        summ = sum(candies)
        ans = 0
        
        if summ<k:
            return 0

        l,r = 1,summ//k

        while l<=r:
            
            mid = (l+r)//2
            count = 0

            for pile in candies:
                count+=(pile//mid)

            if count>=k:
                l = mid+1
                ans = max(ans,mid)
            else:
                r = mid-1

        return ans