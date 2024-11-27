class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = deque()
        for directory in path:
            if directory == '.' or directory == '':
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        return '/' if not stack else ('/'+'/'.join(stack))


        