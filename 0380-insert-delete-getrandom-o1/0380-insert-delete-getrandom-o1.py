class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            print(self.list)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx_del = self.dict[val]
            self.list[idx_del] = self.list[-1]
            self.dict[self.list[-1]] = idx_del
            del self.dict[val]
            self.list.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()