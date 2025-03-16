# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,ans):
        if not root:
            ans.append('')
            return 

        ans.append(root.val)
        self.dfs(root.left,ans)
        self.dfs(root.right,ans)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []

        self.dfs(p,ans1)
        self.dfs(q,ans2)

        return ans1==ans2

