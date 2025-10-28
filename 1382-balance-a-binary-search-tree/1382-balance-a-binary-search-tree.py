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

        def balance(start,end):
            if start > end:
                return None

            mid = (start+end) // 2
            node = TreeNode(arr[mid])

            node.left = balance(start,mid-1)
            node.right = balance(mid+1,end)

            return node
        return balance(0,len(arr) - 1)

            

        

        