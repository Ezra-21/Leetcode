class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        arr = path.split('/')

        for val in arr:
            if val == '..':
                if stack:
                    stack.pop()
            elif val == '.' or val == '':
                continue
            else:
                stack.append(val)
        
        return '/'+'/'.join(stack)