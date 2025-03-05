class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for val in s:
            if val == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(val)

        return ''.join(stack)
