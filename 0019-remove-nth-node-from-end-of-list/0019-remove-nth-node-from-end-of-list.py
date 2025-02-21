# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left,right = head,head
        position = 0
        temp = head
        while right:
            if position+1 > n:
                temp = left
                left = left.next
            position+=1

            right = right.next
        
        if position == n:
            return head.next

        temp.next = left.next

        return head
