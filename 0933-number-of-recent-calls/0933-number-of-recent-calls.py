class RecentCounter:

    def __init__(self):
        self.arr = []
        self.startindex = 0
        

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while self.arr[self.startindex]<t-3000:
            self.arr.pop(self.startindex)
        return len(self.arr)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)