# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        left,right = l1,l2
        remain = 0
        while left and right:
            summ = left.val + right.val + remain
            remain = 0
            if summ>=10:
                remain = 1
                summ = summ%10
            new = ListNode(summ)
            temp.next = new
            temp = temp.next
            left = left.next
            right = right.next

        while left:
            summ = left.val + remain
            remain = 0
            if summ>=10:
                remain = 1
                summ = summ%10
            new = ListNode(summ)
            temp.next = new
            temp = temp.next
            left = left.next


        while right:
            summ = right.val + remain
            remain = 0
            if summ>=10:
                remain = 1
                summ = summ%10
            new = ListNode(summ)
            temp.next = new
            temp = temp.next
            right = right.next

        if remain:
            new = ListNode(remain)
            temp.next = new


        return dummy.next

