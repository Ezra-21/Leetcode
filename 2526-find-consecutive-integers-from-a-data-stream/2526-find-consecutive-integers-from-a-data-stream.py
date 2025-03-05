class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.arr = []
        self.i = 0
        self.j = 0

    def consec(self, num: int) -> bool:
        if num!=self.value:
            self.j = self.i+1
        self.i+=1
        if (self.i-self.j)==self.k:
            self.j+=1
            return True
        return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)