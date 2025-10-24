# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        odd = False
        while queue:
            n = len(queue)
            if odd:
                i,j = 0,len(queue)-1
                while i<j:
                    queue[i].val,queue[j].val = queue[j].val,queue[i].val
                    i+=1
                    j-=1
                odd = False
            else:
                odd = True
            
            while n:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n-=1
        return root
            
