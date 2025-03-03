# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1,head2 = None,None
        

        while l1:
            node = l1.next
            l1.next = head1
            head1 = l1
            l1 = node
            
        while l2:
            node = l2.next
            l2.next = head2
            head2 = l2
            l2 = node
        
        dummy = ListNode(None)
        head = dummy
        remain = 0
        while head1 and head2:
            summ = head1.val+head2.val+remain
            res = summ%10
            remain = summ//10
            new_node = ListNode(res)
            new_node.next = head.next
            head.next = new_node
            head1 = head1.next
            head2 = head2.next

        while head1:
            summ = head1.val+remain
            res = summ%10
            remain = summ//10
            new_node = ListNode(res)
            new_node.next = head.next
            head.next = new_node
            head1 = head1.next
        while head2:
            summ = head2.val+remain
            res = summ%10
            remain = summ//10
            new_node = ListNode(res)
            new_node.next = head.next
            head.next = new_node
            head2 = head2.next
        
        if remain == 1:
            new_node = ListNode(1)
            new_node.next = head.next
            head.next = new_node
            
        
        return dummy.next




        