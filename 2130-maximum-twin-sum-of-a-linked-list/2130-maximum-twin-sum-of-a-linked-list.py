# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(-1)
        curr = head
        size = 0
        while curr:
            new_node = ListNode(curr.val)
            new_node.next = dummy
            dummy = new_node
            curr = curr.next
            size+=1

        ans = float('-inf')
        i = 0
        print(head.val,dummy.val)
        while i<size//2:
            summ = head.val+dummy.val
            ans = max(ans,summ)
            head = head.next
            dummy = dummy.next
            i+=1

        return ans
            
