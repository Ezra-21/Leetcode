class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = min(ranks)
        right = max(ranks)*((cars)**2)
        ans = right
        while left<=right:
            mid = (right+left)//2
            count = 0
            for val in ranks:
                res = int(math.sqrt((mid//val)))
                if count<=cars:
                    count+=res
                else:
                    break
            
            if count>cars:
                right = mid-1
                ans = min(ans,mid)
            elif count<cars:
                left = mid+1
            else:
                right = mid-1
                ans = min(ans,mid)


        return ans
                                            