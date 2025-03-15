# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = True
        ans = []
        if not root:
            return ans
        queue = deque([root])
        while queue:
            n = len(queue)
            temp = []
            while n>0:
                value = queue.popleft()
                temp.append(value.val)
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
                n-=1
            if flag:
                ans.append(temp)
                flag = False
            else:
                ans.append(temp[::-1])
                flag = True

        return ans
                