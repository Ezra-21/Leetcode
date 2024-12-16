class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event = []
        for load,start,end in trips:
            event.append([start,load])
            event.append([end,-load])

        event.sort()
        contain = 0
        for location,change in event:
            contain+=change
            if contain>capacity:
                return False
        return True
