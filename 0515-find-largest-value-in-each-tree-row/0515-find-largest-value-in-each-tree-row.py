# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        queue = deque([root])
        while queue:
            n = len(queue)
            maxi = float('-inf')
            while n>0:
                temp = queue.popleft()
                maxi = max(maxi,temp.val)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                n-=1
            ans.append(maxi)

        return ans
                