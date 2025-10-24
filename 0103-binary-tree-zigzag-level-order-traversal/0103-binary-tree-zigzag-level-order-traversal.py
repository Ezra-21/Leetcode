# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        odd = False
        while queue:
            n = len(queue)
            if odd:
                i,j = 0,len(queue)-1
                while i<j:
                    queue[i].val,queue[j].val = queue[j].val,queue[i].val
                    i+=1
                    j-=1
                odd = False
            else:
                odd = True
            
            temp = []
            while n:
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n-=1
            ans.append(temp)
        return ans
            
