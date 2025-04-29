# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        c = 0
        for node in lists:
            if node:
                heappush(heap, (node.val,c, node))
                c+=1
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val,_,node = heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heappush(heap, (node.next.val,c, node.next))
                c+=1

            
        return dummy.next

        