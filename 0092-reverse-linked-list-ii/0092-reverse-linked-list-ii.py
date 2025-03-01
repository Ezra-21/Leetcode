# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:   
        dummy = ListNode(-1)
        curr1,curr2 = head,head
        idx1,idx2 = 1,1
        while curr1:
            if left<=idx1<=right:
                new = ListNode(curr1.val)
                new.next = dummy
                dummy = new
            elif idx1>right:
                break
            idx1+=1
            curr1 = curr1.next
        
        while curr2:
            if left<=idx2<=right:
                curr2.val = dummy.val
                dummy = dummy.next
            elif idx2>right:
                break
            idx2+=1
            curr2 = curr2.next

        return head

        

    