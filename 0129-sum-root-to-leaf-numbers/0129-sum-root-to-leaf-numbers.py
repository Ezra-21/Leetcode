# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(root,summ):
            if not root.left and not root.right:
                ans.append(summ*10+root.val)
                return

            val = root.val
            if root.left:
                dfs(root.left,summ*10+val)
            if root.right:
                dfs(root.right,summ*10+val)

        dfs(root,0)
        print(ans)
        return sum(ans)


        