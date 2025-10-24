# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0
        
        while queue:
            n = len(queue)
            collect = []

            for _ in range(n):
                val = queue.popleft()
                collect.append(val)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            
            if level%2==1:
                left,right = 0,len(collect)-1
                while left<right:
                    collect[left].val,collect[right].val = collect[right].val,collect[left].val
                    left+=1
                    right-=1
            level+=1

        return root



