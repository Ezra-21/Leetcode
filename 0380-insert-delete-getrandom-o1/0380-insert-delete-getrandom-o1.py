class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            del self.dict[val]
            self.list.pop(idx)
            for i in range(idx,len(self.list)):
                self.dict[self.list[i]] -= 1
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