# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return 0,0

            left,i = dfs(root.left)

            right,j = dfs(root.right)

            summ = left+right+root.val

            fre = i+j+1

            if summ//fre == root.val:
                ans+=1

            return summ, fre

        dfs(root)

        return ans






        