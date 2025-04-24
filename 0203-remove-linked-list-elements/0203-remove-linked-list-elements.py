# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        while head:
            if head.val != val:
                node = ListNode(head.val)
                curr.next = node
                curr = curr.next
            head = head.next
        return dummy.next