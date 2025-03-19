# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = root1.val+root2.val
        elif root1:
            node = root1.val
        elif root2:
            node = root2.val
        else:
            return None
        
        left,right = None,None
        left1,right1 = None,None

        if root1:
            left = root1.left
            right = root1.right
        if root2:
            left1 = root2.left
            right1 = root2.right

        root = TreeNode(node)

        root.left = self.mergeTrees(left,left1)
        root.right = self.mergeTrees(right,right1)

        return root