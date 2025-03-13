class Linked:
    def __init__(self, val):
        self.next = None
        self.val = val

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dummy = Linked(1)
        curr = dummy
        for i in range(2, n + 1):
            node = Linked(i)
            curr.next = node
            curr = node
        curr.next = dummy  

        curr = dummy  

        temp = curr
        

        while n > 1:
            for _ in range(k - 1):
                temp = curr
                curr = curr.next

            temp.next = curr.next  
            curr = temp.next  
            n -= 1  

        return curr.val  