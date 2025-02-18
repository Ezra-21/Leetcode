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
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)





'''

class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]  # Prefix product (1 as identity)
        self.last_zero = -1  # Track last zero index

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # Reset prefix product
            self.last_zero = len(self.prefix) - 1  # Track last zero position
        else:
            self.prefix.append(self.prefix[-1] * num)  # Multiply last value

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  # If `k` exceeds available values, return 0
            return 0
        return self.prefix[-1] // self.prefix[-k-1]  # Compute product efficiently


# Example usage:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))  # Output: 20 (5 * 4)
print(obj.getProduct(3))  # Output: 0 (Contains 0)
print(obj.getProduct(4))  # Output: 0 (Contains 0)
obj.add(8)
print(obj.getProduct(2))  # Output: 32 (4 * 8)
'''