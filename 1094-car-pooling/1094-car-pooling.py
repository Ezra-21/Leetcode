class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0]*1001
        for passenger,start,end in trips:
            prefix[start] += passenger
            prefix[end] -= passenger

        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]

        for num in prefix:
            if num>capacity:
                return False

        return True
        