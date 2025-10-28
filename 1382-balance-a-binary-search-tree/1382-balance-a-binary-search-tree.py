# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)

        def balance(arr):
            if not arr:
                return None

            mid = len(arr) // 2
            node = TreeNode(arr[mid])

            node.left = balance(arr[:mid])
            node.right = balance(arr[mid+1:])

            return node
        return balance(arr)

            

        

        