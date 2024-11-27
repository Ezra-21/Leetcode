class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)