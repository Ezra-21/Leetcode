# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(-1)
        node.next = head
        head = node
        curr = head
        temp = head
        while curr:
            if curr.val == val:
                temp.next = curr.next
                curr = curr.next
                continue
            temp = curr
            curr = curr.next
        return head.next

        
