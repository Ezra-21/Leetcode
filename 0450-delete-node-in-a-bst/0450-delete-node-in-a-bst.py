# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self,head):
        if not head.left:
            return head
        return self.find(head.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val>key:
            root.left = self.deleteNode(root.left,key)
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
        else:

            if not root.left and not root.right:
                return root.right
            elif not root.left:
                return root.right   
            elif not root.right:
                return root.left
            else:
                newvalue = self.find(root.right)
                root.val = newvalue.val
                root.right = self.deleteNode(root.right,newvalue.val)
        return root

        
