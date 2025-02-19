# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)
        temp = head
        curr1,curr2 = list1,list2
        while curr1 and curr2:
            if curr1.val>curr2.val:
                temp.next = curr2
                temp = temp.next
                curr2 = curr2.next
            else:
                temp.next = curr1
                temp = temp.next
                curr1 = curr1.next

        while curr1:
            temp.next = curr1
            temp = temp.next
            curr1 = curr1.next

        while curr2:
            temp.next = curr2
            temp = temp.next
            curr2 = curr2.next

        head = head.next
        return head
        