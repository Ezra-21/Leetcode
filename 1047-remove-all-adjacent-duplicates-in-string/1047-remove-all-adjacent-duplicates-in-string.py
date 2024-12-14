class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if stack[-1] == char:
                    stack.pop()
                else:
                    stack.append(char)

        return ''.join(stack)
        