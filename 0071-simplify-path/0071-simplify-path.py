from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        components = path.split('/')  # Split the path by '/' into components
        
        for component in components:
            if component == '' or component == '.':
                # Ignore empty components or '.' (current directory)
                continue
            elif component == '..':
                # '..' means go up one directory, so pop from stack if it's not empty
                if stack:
                    stack.pop()
            else:
                # Add valid directory names to the stack
                stack.append(component)
        
        # Join the stack into the simplified path
        return '/' + '/'.join(stack)
