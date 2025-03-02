class MyStack:

    def __init__(self):
        self.stack = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size+=1

    def pop(self) -> int:
        num = self.stack.pop()
        self.size-=1
        return num

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.size==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()