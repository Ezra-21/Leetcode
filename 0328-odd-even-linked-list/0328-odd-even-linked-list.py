# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head

        curr_o = head
        curr_e = head.next
        even_head = curr_e

        while curr_e and curr_e.next:
            curr_o.next = curr_e.next
            curr_o = curr_o.next

            curr_e.next = curr_o.next
            curr_e = curr_e.next

        curr_o.next = even_head

        return head
        