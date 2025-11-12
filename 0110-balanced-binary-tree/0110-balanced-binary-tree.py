# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, head: Optional[TreeNode]) -> bool:
        flag = True
        def helper(root):
            nonlocal flag
            if not root:
                return 0
                
            left = helper(root.left)+1
            right = helper(root.right)+1
            if abs(left-right)>1:
                flag = False


            return max(left,right)
        helper(head)
        return flag
        