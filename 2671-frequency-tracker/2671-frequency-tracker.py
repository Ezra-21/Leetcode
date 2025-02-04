class FrequencyTracker:

    def __init__(self):
        self.hashh = Counter()
        self.fre = Counter()

    def add(self, number: int) -> None:
        pre = self.hashh[number]
        self.fre[pre]-=1
        self.hashh[number]+=1
        self.fre[self.hashh[number]] += 1
        

    def deleteOne(self, number: int) -> None:
        if number in self.hashh:
            pre = self.hashh[number]
            self.fre[pre]-=1
            self.hashh[number]-=1
            if self.hashh[number]==0:
                del self.hashh[number]
            
            self.fre[self.hashh[number]] += 1
            
            
    def hasFrequency(self, frequency: int) -> bool:
        return self.fre[frequency]>0
        
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)