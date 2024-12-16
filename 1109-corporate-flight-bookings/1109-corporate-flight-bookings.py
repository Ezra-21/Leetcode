class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for start,end,seat in bookings:
            ans[start-1]+=seat
            ans[end]-=seat
        
        for i in range(1,len(ans)):
            ans[i]+=ans[i-1]

        return ans[:n]


        