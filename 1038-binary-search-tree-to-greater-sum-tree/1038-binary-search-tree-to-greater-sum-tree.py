# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def dfs(self,node):
        if not node:
            return
        self.dfs(node.right)
        self.sum+=node.val
        node.val = self.sum
        self.dfs(node.left)
        return self.sum


    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root

        