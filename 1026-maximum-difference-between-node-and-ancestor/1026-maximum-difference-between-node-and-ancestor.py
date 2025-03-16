# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,Max,Min):
        if not root:
            return Max - Min

        Max = max(Max,root.val)
        Min = min(Min,root.val)

        left = self.solve(root.left,Max,Min)
        right = self.solve(root.right,Max,Min)

        return max(right,left)


    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        Max,Min = float('-inf'),float('inf')
        return self.solve(root,Max,Min)