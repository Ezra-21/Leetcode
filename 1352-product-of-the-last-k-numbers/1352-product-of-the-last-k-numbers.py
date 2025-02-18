class ProductOfNumbers:
    def __init__(self):
        self.temp = 1
        self.prefix = []

    def add(self, num: int) -> None:
        if num==0:
            self.temp = 1
            self.prefix = []
        else:
            self.prefix.append(self.temp*num)
            self.temp = self.prefix[-1]
            
    def getProduct(self, k: int) -> int:
        if k>len(self.prefix):
            return 0
        if k==len(self.prefix):
            return self.prefix[-1]

        return self.prefix[-1]//self.prefix[-k-1]
        
