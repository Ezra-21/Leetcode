# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
        