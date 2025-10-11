class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        last = self.head.prev  

        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node

    def delete(self, key):
        if self.head.data == key:
            last = self.head.prev
            self.head = self.head.next
            self.head.prev = last
            last.next = self.head
            return

        # Delete middle or end by value
        current = self.head.next
        while current != self.head:
            if current.data == key:
                prev_node = current.prev
                next_node = current.next
                prev_node.next = next_node
                next_node.prev = prev_node
                return
            current = current.next

    def check(self):
        return self.head.next == self.head

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = DoublyCircularLinkedList()
        for i in range(n):
            arr.insert_end(i+1)
        
        current = arr.head
        while not arr.check():
            for _ in range(k-1):
                current = current.next
            temp = current.data
            current = current.next
            arr.delete(temp)

        return current.data


                
        