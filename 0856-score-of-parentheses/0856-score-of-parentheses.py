class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        stack = deque()
        for val in s:
            count = 0
            if val == '(':
                stack.append(0)
            else:
                while stack[-1] != 0:
                    count += stack.pop()
                count = max(2*count,1)
                stack.pop()
                stack.append(count)
        res = sum(stack)
        return res
        