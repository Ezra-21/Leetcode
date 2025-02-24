class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
    def debug(self):
        cur = self.head
        while cur:
            print(cur.val,end=" ")
            cur = cur.next
        print()
        

    def get(self, index: int) -> int:
        cur = self.head.next
        if not cur:
            return -1

        while cur.next and index>0:
            cur = cur.next
            index -= 1
        if index > 0:
            return -1
        return cur.val        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head.next:
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        new_node = Node(val)
        cur.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        cur = self.head.next
        if not cur:
            return
        index -= 1
        while cur.next and index>0:
            cur = cur.next
            index -= 1
        if index > 0:
            return

        new_node = Node(val)
        if index == 1:
            cur.next = new_node
            return
        new_node.next = cur.next
        cur.next = new_node                

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head.next:
                self.head.next = self.head.next.next
            return

        cur = self.head.next
        if not cur:
            return
        index -= 1
        while cur.next and index>0:
            cur = cur.next
            index -= 1
        if index > 0:
            return

        if cur.next and cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)