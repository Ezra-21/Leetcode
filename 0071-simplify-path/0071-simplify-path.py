class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        path = path.split('/')
        for dir in path:
            if dir == '' or dir == '.':
                continue
            elif dir == '..':
                if len(stack)!=0:
                    stack.pop()
            else:
                stack.append(dir)

        return '/'+'/'.join(stack)        