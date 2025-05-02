# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def dfs(self,node):
        if not node:
            return(0,0)

        
        right_sum,right_len = self.dfs(node.right)
        left_sum,left_len = self.dfs(node.left)
        total = node.val+right_sum+left_sum
        length = 1+left_len+right_len

        if node.val ==(total//length):
            self.count+=1

        return total,length
        



    def averageOfSubtree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.count

        