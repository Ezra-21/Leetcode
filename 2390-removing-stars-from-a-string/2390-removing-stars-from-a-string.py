class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for val in s:
            if val == '*':
                stack.pop()
            else:
                stack.append(val)

        return ''.join(stack)
