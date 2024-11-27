class Solution:
    def simplifyPath(self, path: str) -> str:
        class Node:
            def __init__(self,value):
                self.value = value
                self.next = None
        class stack:
            def __init__(self):
                self.head = None
                self.size = 0

            def isempty(self):
                return self.size == 0

            def push(self,value):
                if self.isempty():
                    self.head = Node(value)
                else:
                    node = Node(value)
                    node.next = self.head
                    self.head = node
                self.size += 1

            def pop(self):
                if self.isempty():
                    return None
                else:
                    remove = self.head
                    self.head = remove.next
                    remove.next = None
                    self.size -= 1
                    return remove.value
        stack = stack()
        alpha = []
        dot = ''
        for val in path:
            if val != '/':
                alpha.append(val)
            else:
                if alpha:
                    res = ''.join(alpha)
                    if res == '..':  # Handle '..'
                        stack.pop()
                    elif res[0]!='.' or len(res) >= 2:
                        stack.push(res)
                    alpha = []
                
        if alpha:
            res = ''.join(alpha)
            if res == '..':  # Handle '..'
                stack.pop()
            elif res[0]!='.' or len(res) >= 2:
                    stack.push(res)

        res = ''   
        while not stack.isempty():
            value = stack.pop()
            res = '/' + value + res
        return res if res else '/'

                
